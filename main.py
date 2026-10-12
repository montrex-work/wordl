import curses
import locale
import os

os.environ.setdefault("ESCDELAY", "25")
locale.setlocale(locale.LC_ALL, "")


def draw(stdscr, text, erase_each_frame, last_key):
    if erase_each_frame:
        stdscr.erase()                      # blank the desired grid
    h, w = stdscr.getmaxyx()
    if h < 20 or w < 50:
        stdscr.addstr(0, 0, "Window too small (need 50x20)"[:w - 1])
        stdscr.refresh()
        return

    # 1. status line
    mode = "ON " if erase_each_frame else "OFF"
    stdscr.addstr(0, 0, f"Esc=quit  Tab=toggle erase() (now {mode})  last key: {last_key!r}"[:w - 1])

    # 2. addstr with (y, x), then without: it continues at the cursor
    stdscr.addstr(1, 0, "A")                # moves to (1,0) and writes
    stdscr.addstr(" B")                     # no coords -> continues right after "A"
    y, x = stdscr.getyx()                   # where is the cursor now?
    stdscr.addstr(f"  <- cursor is at (y={y}, x={x})")

    # 3. \n inside a string: next line starts at column 0, not at x=30
    stdscr.addstr(3, 0, "newline demo ->")
    stdscr.addstr(3, 30, "ab\ncd")          # "cd" lands on row 4, column 0

    # 4. wrapping at the right edge
    stdscr.addstr(5, w - 4, "WRAPPED")      # "WRAP" fits, "PED" wraps to row 6, col 0

    # 5. the centered box, drawn manually
    box_h, box_w = h // 3, w // 2
    top, left = (h - box_h) // 2, (w - box_w) // 2
    stdscr.addstr(top, left, "┌" + "─" * (box_w - 2) + "┐")
    for row in range(top + 1, top + box_h - 1):
        stdscr.addstr(row, left, "│")
        stdscr.addstr(row, left + box_w - 1, "│")
    stdscr.addstr(top + box_h - 1, left, "└" + "─" * (box_w - 2) + "┘")

    # 6. typed text, wrapped to the box width, last lines only
    inner_w, inner_h = box_w - 2, box_h - 2
    lines = [text[i:i + inner_w] for i in range(0, len(text) + 1, inner_w)]
    visible = lines[-inner_h:]
    for i, line in enumerate(visible):
        stdscr.addstr(top + 1 + i, left + 1, line)

    # 7. move() only places the cursor, so the blinking cursor follows the text
    stdscr.move(top + len(visible), left + 1 + len(visible[-1]))

    stdscr.refresh()                        # one refresh: diff and send


def main(stdscr):
    text, erase_each_frame, last_key = "", True, None
    draw(stdscr, text, erase_each_frame, last_key)

    while True:
        key = stdscr.get_wch()
        last_key = key

        if key == "\x1b":                   # Esc
            break
        elif key == "\t":                   # Tab: toggle erase()
            erase_each_frame = not erase_each_frame
        elif key == curses.KEY_RESIZE:
            pass
        elif key in (curses.KEY_BACKSPACE, "\x7f", "\b"):
            text = text[:-1]
        elif isinstance(key, str) and key.isprintable():
            text += key

        draw(stdscr, text, erase_each_frame, last_key)


curses.wrapper(main)

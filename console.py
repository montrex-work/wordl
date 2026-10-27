def _ansii_fg_color(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"
    

def pause():
    input("Press enter to continue...")


def clear():
    print("\033[2J\033[H", end="", flush=True)


def printc(text: str, width: int):
    print(f'{text:^{width}}')
    

class color:
    reset = "\033[0m"

    red      = _ansii_fg_color(255, 0, 0)
    yellow   = _ansii_fg_color(106, 170, 100)
    green    = _ansii_fg_color(201, 180, 88)
    darkgrey = _ansii_fg_color(58, 58, 60)
    grey     = _ansii_fg_color(86, 87, 88)

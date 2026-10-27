import os  
import random
from enum import Enum, auto

import console as cs
from console import color as c



# TODO 
'''

implement using alternet buffer
'''



# tools

class IO:
    def loadCSV(file: str) -> list|dict:
        return {} # TODO: implement




class State(Enum): 
    MAIN_MENU = auto()
    SETTINGS  = auto()
    GAME      = auto()
    EXIT      = auto()


class Settings:
    # box drawing: modern / basic (works anywhere)


    ... # TODO: implement
    


class Wordle:
    def __init__(self) -> None:
        self.state = State.MAIN_MENU 
        self.word_list = []

        
    def gameSetup(self):
        self.guess_list = {_:'' for _ in range(6)}
        self.secret = 'plane'# TODO: random select


    def loop(self) -> None:
        while self.state != State.EXIT:
            match self.state:
                case State.MAIN_MENU: self.menu()
                case State.SETTINGS: self.settings()
                case State.GAME: self.game()

        cs.clear()
        exit(0)

        
    def menu(self):
        wid, hig = os.get_terminal_size()
        cs.clear()

        lines = 16
        print('\n' * int(hig/2 - lines/2))

        title = '''    
 _ _ _ _____ _____ ____  __    _____ 
| | | |     | __  |    \|  |  |   __|
| | | |  |  |    -|  |  |  |__|   __|
|_____|_____|__|__|____/|_____|_____|
        '''

        for line in title.splitlines():
            cs.printc(line, wid)
        
        '''
        cs.printc("+---------------+", wid)
        cs.printc("|  1| PLAY      |", wid)
        cs.printc("|  2| SETTINGS  |", wid)
        cs.printc("|  3| EXIT      |", wid)
        cs.printc("+---------------+", wid)
        '''

        # ─ │ ╭ ╮ ╰ ╯
        cs.printc("╭───────────────╮", wid)
        cs.printc("│  1| PLAY      │", wid)
        cs.printc("│  2| SETTINGS  │", wid)
        cs.printc("│  3| EXIT      │", wid)
        cs.printc("╰───────────────╯", wid)
        
        
        print()      
        user = input(' ' * int(wid / 2 - 17/2) + '➜ ').strip()

        if user not in ['1','2','3']:
            print('\033[1A', ' ' * int(wid / 2 - 17/2 - 1) + f'➜ {user}{c.red} <- Wrong input!{c.reset}')

            cs.pause()

        else:
            match int(user):
                case 1: self.state = State.GAME
                case 2: self.state = State.SETTINGS
                case 3: self.state = State.EXIT


    def settings(self):
        # Settins:
        # set word
        # style
        
        lines = 10
        print('\n' * int(hig/2 - lines/2))
        cs.pause()


    def game(self):
        # Setup game:
        # get a random word
        # reset guess list

        
        lines = 10
        print('\n' * int(hig/2 - lines/2))

        # draw board rows
        # draw keboard ???
        # input

        self.guess_list[0] = 'apple'
        for guess in self.guess_list.items:
            asd = self.cechk(guess) # y--gg

        cs.pause()


            

# test
if __name__ == '__main__':
    app = Wordle()
    app.loop()

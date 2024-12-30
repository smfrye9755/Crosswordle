import random
import sys
from termcolor import colored, cprint
import os


clear = False
printed = False

wins = 0
losses = 0


def print_instructions():
    print("How to play:")
    print("Type a 5 letter word and hit enter.")

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)   

def print_board(board):
    for word in board:
        print(word)


"""def color_print(cw):
    print(cw[0] + cw[1] + cw[2] + cw[3] + cw[4])"""

def check_word(inp, word):
    word_check = ''
    for i in range(5):
        if inp[i] == word[i]:
            word_check += colored(inp[i], on_color="on_green")
        elif inp[i] in word:
            word_check += colored(inp[i], on_color="on_yellow")
        else:
            word_check += colored(inp[i],on_color= "on_grey")
    return word_check



def new_game():
    
    print_instructions()
    word = read_random_word()    
    board = []
    guess = 1

    while guess < 7:
        
        inp = input().lower()
        if clear:
            os.system('cls' if os.name == 'nt' else 'clear')

        if len(inp) != 5:
            print("A word must be 5 letters long")
            print_board(board)
            continue
         
        if word == inp:
            print_board(board)
            cprint(word, 'white', 'on_green') 
            print("YOU WIN!")
            print('You took', guess, "guesses!")
            return
        
        color_word = check_word(inp, word)
        
        board += [color_word]
        print_board(board)
        guess += 1
        


while(True):
    if not printed:
        print('To start a new game type: "'+ colored('start', 'green') + '", to quit type"'+ colored('exit', 'yellow') + '".')
        print('WARNING: by default this game will', colored('NOT', 'red'), 'clear your terminal.')
        print('This can lead to cluttering after multiple games.')
        print('To enable terminal clearing at the start of each game type "clear".')
        print('If you want to turn off clearing, type "no clear".')
        printed = True
    start = input().lower()
    if start == "start":
        printed = False
        new_game()
        
    if start == "exit" or start == "quit":
        sys.exit(0)
    if start == "no clear": 
        clear = False
        print('Clearing disabled')
    if start == "clear":
        clear = True
        print('Clearing enabled')



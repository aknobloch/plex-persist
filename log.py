import sys

RED   = '\033[1;31m'  
BLUE  = '\033[1;34m'
CYAN  = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD    = '\033[;1m'
REVERSE = '\033[;7m'

def __change_color(color) :

    sys.stdout.write(color)

def __reset_color() :

    sys.stdout.write(RESET)

def info(message) :

    print(message)

def debug(message) :

    __change_color(BOLD)
    print(message)
    __reset_color()

def error(message) :

    __change_color(RED)
    print(message)
    __reset_color()

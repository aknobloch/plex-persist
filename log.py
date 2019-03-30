import sys
from constants import TextStyle, LogLevel

__LOG_LEVEL = LogLevel.INFO

def __change_color(color) :

    sys.stdout.write(color)

def __reset_color() :

    sys.stdout.write(TextStyle.RESET)

def enable_debug() :

    __LOG_LEVEL = LogLevel.DEBUG

def info(message) :

    print(message)

def debug(message) :

    if __LOG_LEVEL != LogLevel.DEBUG :
        return

    __change_color(TextStyle.BOLD)
    print(message)
    __reset_color()

def error(message) :

    __change_color(TextStyle.RED)
    print(message)
    __reset_color()

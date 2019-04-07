import sys
from logging import exception as log_exception
from model.constants import TextStyle, LogLevel

class log() :

    __LOG_LEVEL = LogLevel.INFO

    def __change_color(color) :

        sys.stdout.write(color)

    def __reset_color() :

        sys.stdout.write(TextStyle.RESET)

    def enable_debug() :

        log.__LOG_LEVEL = LogLevel.DEBUG

    def info(message) :

        print(message)

    def debug(message) :

        if log.__LOG_LEVEL != LogLevel.DEBUG :
            return

        log.__change_color(TextStyle.BOLD)
        print(message)
        log.__reset_color()

    def error(message) :

        log.__change_color(TextStyle.RED)
        print(message)
        log.__reset_color()

    def exception(message) :

        log.__change_color(TextStyle.RED)
        log_exception(message)
        log.__reset_color()

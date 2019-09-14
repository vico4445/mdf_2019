import sys


def show(value):
    sys.stderr.write(str(value))
    breakline()


def breakline():
    sys.stderr.write("\n")


def show_break(stringvalue):
    show(stringvalue)
    breakline()
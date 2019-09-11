import sys


def show(stringvalue):
    sys.stderr.write(stringvalue)


def breakline():
    sys.stderr.write("\n")


def show_break(stringvalue):
    show(stringvalue)
    breakline()
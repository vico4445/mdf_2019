import debug
# TODO : Attention il se peut que la sortie est une chaine de caractere pas uns liste ?
import sys


def input_as_list():
    lines = []
    while True:
        input_val = input().rstrip('\n')
        if not input_val:
            break
        lines.append(input_val)
    return lines


def main():
    lines = input_as_list()
    debug.show('Input : [' + ','.join(lines) + ']')

    # Code
    # Constant cast
    # lines = [int(elem) for elem in lines]  # Cast lines values in wanted type !!!

    # Start of code
    print('test')

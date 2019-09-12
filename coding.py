import debug
# TODO : pouvoir print n'importe quel type d'objet dans show.debug() !!!


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
    debug.show('Input : [' + ','.join(lines) + '] \n')

    # Code
    # Constant cast
    lines = [int(elem) for elem in lines]  # Cast lines values in wanted type !!!

    # Start of code
    print('')






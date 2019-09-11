import debug


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

    # Start of code
    lines = [int(elem) for elem in lines]  # Cast lines values in wanted type !!!
    couleurs = ['orange', 'jaune', 'vert', 'rose', 'bleu', 'violet']
    print(couleurs[(5 + sum(lines)) % 6])






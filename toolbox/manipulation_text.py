import re


def regex_example():
    txt = "The rain in Spain"
    x = re.search("^The (.*) Spain$", txt)
    print(x.group(0))  # -->  The rain in Spain
    print(x.group(1))  # --> rain in


def letter_to_int_example():
    ord('a')+1 == ord('b')


def get_all_substrings(input_string, max_size=None):
    if max_size is None: max_size = len(input_string)
    length = len(input_string)
    return [input_string[i:j+1] for i in range(length) for j in range(i, length) if j+1-i <= max_size]


if __name__ == '__main__':
    print(get_all_substrings('test'))

import functools

FILE_NAME = 'text/names.txt'


def print_longest():
    with open(FILE_NAME, 'r') as input_file:
        print(max(input_file.read().split('\n')))


def print_len_sum():
    with open(FILE_NAME, 'r') as input_file:
        # option 1
        print(sum(len(name) for name in input_file.read().split('\n')))
        # option 2
        print(len(''.join(name for name in input_file.read().split('\n'))))
        # option 3
        print(len(functools.reduce(lambda a, b: a + b, input_file.read().split('\n'))))


def print_len_min():
    with open(FILE_NAME, 'r') as input_file:
        names_list = input_file.read().split('\n')
        min_len = len(min(names_list, key=len))
        print('\n'.join([name for name in names_list if len(name) == min_len]))


def create_len_file():
    with open(FILE_NAME, 'r') as input_read:
        with open(r'text\name_length.txt', 'w') as input_write:
            input_write.write('\n'.join([str(len(item)) for item in input_read.read().split('\n')]))


def print_name_length():
    while True:
        try:
            length = int(input('Enter name length:\t'))
            with open(FILE_NAME, 'r') as input_file:
                # option 1
                print('\n'.join(list(filter(lambda e: len(e) == length, input_file.read().split('\n')))))
                # option 2
                print('\n'.join([item for item in input_file.read().split('\n') if len(item) == length]))
            break
        except ValueError:
            print('Invalid input. Pls Enter Only Numbers')


print_len_sum()
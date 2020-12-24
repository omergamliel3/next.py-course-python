import functools


def combine_coins(coin='', numbers=[]):
    return ', '.join([str(item) + coin for item in numbers])


def double_letter_list_comp(my_str=''):
    return ''.join([letter * 2 for letter in my_str])


def double_letter(my_str=''):
    return ''.join(list(map(lambda e: e * 2, my_str)))


def four_dividers(num):
    return list(filter(lambda e: e % 4 == 0, range(1, num + 1)))


def sum_of_digits(num=0):
    return functools.reduce(lambda a, b: int(a) + int(b), list(str(num)), 0)


def function(num, item):
    return num + 1


def f(numbers):
    return functools.reduce(function, numbers)


print(combine_coins("$", [1, 2, 3, 4]))
print(double_letter_list_comp('omer'))

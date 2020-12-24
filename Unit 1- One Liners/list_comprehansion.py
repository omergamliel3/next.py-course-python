def intersection(list_1=[], list_2=[]):
    return list(set(list_1).intersection(set(list_2)))


def is_prime(num):
    return num % 2 != 0 and num % 3 != 0


def is_funny(string=''):
    return all([True if char.lower() == 'h' or char.lower() == 'a' else False for char in string])
    # return all(list(map(lambda char: char.lower() == 'h' or char.lower() == 'a', string)))


print(is_funny('ahahahah'))

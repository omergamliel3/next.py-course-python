# define custom exceptions

# length error exception
class LengthError(Exception):
    def __init__(self, arg):
        self._arg = arg
        super().__init__(arg)

    def __str__(self):
        return f'id number must equal to 9. Current length: {len(self._arg)}'


# type error exception
class TypeError(Exception):
    def __init__(self, arg):
        self._arg = arg
        super().__init__(arg)

    def __str__(self):
        errMsg = f'id number must be a string or an integer. Current type: {type(self._arg).__name__}'
        return errMsg


class IDIterator:
    def __init__(self, id):
        # make sure that id is a valid id number
        check_id_valid(id)
        # make sure that id is integer
        self._id = int(id)

    # implementing "Iterator Protocol"

    # return self
    def __iter__(self):
        return self

    # return the next valid id number after the current id
    def __next__(self):
        # stop iteration when id is equal to 999999999
        if self._id == 999999999:
            raise StopIteration()
        valid = False
        # while id is not valid, try to validate the next id
        # if id is valid, return the id
        while not valid:
            self._id += 1
            valid = check_id_valid(self._id)

        return self._id


def validator_helper(id_number):
    """
    a function which takes an id_number and return a list of type integer,
    after performed id validation operations on the list elements 
    """
    # a list which contains all numbers from id_number
    numbers = []
    # iterate id_number
    for index, number in enumerate(id_number):
        # multiply by 1 for even index position
        if index % 2 == 0:
            multiply = 1
        # multiply by 2 for odd index position
        else:
            multiply = 2
        # convert number to integer multiply
        value = int(number) * multiply
        # if value is greater that 9, combine the two numbers (11 = 1+1)
        if value > 9:
            value = int(str(value)[0]) + int(str(value)[1])
        # append value to numbers list
        numbers.append(value)
    # return numbers list
    return numbers


def check_id_valid(id_number):
    """
    a function which vaildate an israeli id number

    """
    # id_number argument target type validation
    if not isinstance(id_number, (str, int)):
        raise TypeError(id_number)

    # make sure that id_number parameter is a type str
    id_number = str(id_number)
    # length validation check
    if not len(id_number) == 9:
        raise LengthError(id_number)

    # perform id validation operations
    numbers = validator_helper(id_number)

    # return true / false whatever the sum of
    # numbers list is divided by 10 without residue
    return sum(numbers) % 10 == 0


def id_generator(id_number):
    """
    a generator function which returns valid IDs
    after id_number argument
    """
    # make sure the type is an integer
    id = int(id_number)
    # make sure the id is valid
    check_id_valid(id_number)
    # stop iteration when id is greater then 999999999
    while id <= 999999999:
        # increment id
        id += 1
        # validate id
        valid = check_id_valid(id)
        # if valid, yield id
        # if not valid continue to another while loop
        if valid:
            yield id


def main():
    id = 123456780
    # create an IDIterator instance
    valid_id_iter = iter(IDIterator(id))
    # produce 10 valid id numbers from iter
    for _ in range(0, 10):
        print(next(valid_id_iter))

    print('\n\n\n')

    # create an id generator instance
    id_gen = id_generator(id)
    for _ in range(0, 10):
        print(next(id_gen))


if __name__ == "__main__":
    main()

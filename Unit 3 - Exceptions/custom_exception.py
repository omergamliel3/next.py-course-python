# Create a custom factorial exception
class FactorialArgumentError(Exception):
    def __init__(self, arg) -> None:
        super().__init__(arg)
        self._arg = arg

    def __str__(self) -> str:
        return f"Provided argument {self._arg} is not a positive integer."


def factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise FactorialArgumentError(n)
    except FactorialArgumentError as err:
        print(err)
    else:
        fact = 1
        for i in range(n, 0, -1):
            fact *= i
        return fact


class UderAge(Exception):
    def __init__(self, age) -> None:
        super().__init__(age)
        self._age = age

    def __str__(self):
        difference = 18 - self._age
        year = ''
        if difference == 1:
            year = 'year'
        else:
            year = 'years'

        return f'You age ({self._age}) is under 18. You will be invited in {difference} {year}'


def send_initation(name, age):
    try:
        if int(age) < 18:
            raise UderAge(int(age))
    except UderAge as err:
        print(err)
    else:
        print('You should send an invite to %s' % name)


def main():
    print(factorial(-1))
    send_initation("omer", 21)
    send_initation("yuval", 16)


if __name__ == "__main__":
    main()

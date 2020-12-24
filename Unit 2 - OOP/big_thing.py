class BigThing:
    def __init__(self, value):
        self._value = value

    def size(self):
        if isinstance(self._value, int):
            return self._value
        if isinstance(self._value, (str, dict, list, set)):
            return len(self._value)


class BigCat(BigThing):
    def __init__(self, value, weight=0):
        super().__init__(value)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return 'Very Fat'
        if self._weight > 15:
            return 'Fat'

        return 'OK'


def main():
    my_thing1 = BigThing(10)
    my_thing2 = BigThing('balloon')

    print(my_thing1.size())
    print(my_thing2.size())

    cutie = BigCat("mitzy", 16)
    print(cutie.size())


if __name__ == "__main__":
    main()

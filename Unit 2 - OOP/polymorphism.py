# superclass
class Animal:
    def __init__(self, name):
        self._name = name
        self._hunger = 0
        self._fun = 0

    def play(self):
        self._fun += 1

    def eat(self):
        if self._hunger > 0:
            self._hunger -= 1

    def __str__(self):
        return f'My name is {self._name} and I am an animal!'

# subclass


class Dog(Animal):
    def __init__(self, name, fur_color):
        # init superclass
        super().__init__(name)
        self._fur_color = fur_color

    def get_fur_color(self):
        return self._fur_color

    def go_for_a_walk(self):
        self._fun += 2

    # override eat method from superclass
    def eat(self):
        super().eat()
        print("eating a bone!")

    # override __str__ method from superclass
    def __str__(self):
        return f'My name is {self._name} and I am a dog!'


def main():
    dog = Dog('Lucky', "Black")
    dog.eat()
    print(dog)

    animal = Animal("Grey")
    animal.eat()
    print(animal)


if __name__ == "__main__":
    main()

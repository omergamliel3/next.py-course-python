# Super class
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

# Sub class, inherite Animal variables and methods


class Dog(Animal):
    def __init__(self, name, fur_color):
        # init super class (Animal)
        # Animal().__init__(name)
        super().__init__(name)
        self._fur_color = fur_color

    def get_fur_color(self):
        return self._fur_color

    def go_for_a_walk(self):
        self._fun += 2


def main():
    dog = Dog('Lucky', "Black")
    dog.eat()
    dog.play()
    dog.get_fur_color()
    dog.go_for_a_walk()

    animal = Animal("Grey")
    animal.play()
    animal.eat()

    print(issubclass(Dog, Animal))
    print(isinstance(dog, Animal))


if __name__ == "__main__":
    main()

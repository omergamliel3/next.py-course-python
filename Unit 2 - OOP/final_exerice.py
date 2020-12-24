class Animal:
    """
    A class used to represent an animal
    """

    def __init__(self, name='', hunger=0):
        """
        initialize name and hunger
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        return name
        """
        return self._name

    def is_hungry(self):
        """
        return true if hunger is more then zero, else return false
        """
        return self._hunger > 0

    def feed(self):
        """
        assgin hunger to zero
        """
        self._hunger = 0

    def talk(self):
        """
        print "talk!"
        """
        print('talk!')

    def unique_act(self):
        pass


class Dog(Animal):
    def talk(self):
        print('woof woof!')

    def unique_act(self):
        print('There you go, sir!')


class Cat(Animal):
    def talk(self):
        print('meow!')

    def unique_act(self):
        print('Meeeeeeow')


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name=name, hunger=hunger)
        self._stink_count = stink_count

    def talk(self):
        print('tssss!')

    def unique_act(self):
        print('Dear lord!')


class Unicorn(Animal):
    def talk(self):
        print('Good day, darling!')

    def unique_act(self):
        print('I\'m not your toy...')


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name=name, hunger=hunger)
        self._color = color

    def talk(self):
        print('Raaaaawr!')

    def unique_act(self):
        print('$@#$#@$')


class Zoo():
    zoo_name = 'Hayaton'

    def __init__(self, zoo_animals):
        self._zoo_animals = zoo_animals

    def set_zoo_animals(self, zoo_animals):
        self._zoo_animals = zoo_animals

    def add_animals(self, animals):
        self._zoo_animals.extend(animals)

    def feed(self):
        for animal in self._zoo_animals:
            if animal.is_hungry():
                print(type(animal).__name__, animal.get_name())
                animal.feed()
                animal.talk()
                animal.unique_act()


def main():
    dog = Dog("Brownie", 10)
    cat = Cat("Zelda", 3)
    skunk = Skunk("Stinky", 0)
    unicorn = Unicorn("Keith", 7)
    dragon = Dragon("Lizzy", 1450)

    animals = [dog, cat, skunk, unicorn, dragon]
    zoo = Zoo(animals)
    zoo.feed()

    new_dog = Dog("Doggo", 80)
    new_cat = Cat("Kitty", 80)
    new_skunk = Skunk("Stinky Jr.", 80)
    new_unicorn = Unicorn("Clair", 80)
    new_dragon = Dragon("McFly", 80)

    new_animals = [new_dog, new_cat, new_skunk, new_unicorn, new_dragon]

    zoo.add_animals(new_animals)

    zoo.feed()

    print(Zoo.zoo_name)


if __name__ == "__main__":
    main()

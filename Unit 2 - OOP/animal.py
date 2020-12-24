class Animal:
    count_animals = 0

    def __init__(self, name='Animal', age=0):
        self._name = name
        self._age = age
        Animal.count_animals += 1

    def __repr__(self) -> str:
        return f'Name: {self._name}\nAge: {self._age}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_age(self, age: int):
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    @classmethod
    def my_animal(cls):
        return cls('Grey', 10)

    @staticmethod
    def class_name() -> str:
        return 'Animal'


def main():
    animal1 = Animal('Grey', 10)
    animal2 = Animal('White', 11)
    animal1.birthday()
    print(f'Animal1: {animal1.get_age()}')
    print(f'Animal2: {animal2.get_age()}')
    print(animal1)
    print(animal2)
    animal3 = Animal.my_animal()
    animal3.birthday()
    animal3.birthday()
    print(animal3)
    print(Animal.class_name())
    animal3.set_age(15)
    animal4 = Animal()
    print(f'Animals count {Animal.count_animals}')


if __name__ == "__main__":
    main()

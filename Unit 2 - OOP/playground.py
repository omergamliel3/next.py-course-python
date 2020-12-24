class Dog:
    # Class Attribute
    species = 'mammal'
    count_dogs = 0

    # Initializer / Instance Attributes
    def __init__(self, name, age=1):
        self._name = name
        self._age = age
        Dog.count_dogs += 1

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_age(self, age):
        self._age = age

    def set_name(self, name):
        self._name = name

    def birth_day(self):
        self._age += 1

    def __str__(self):
        return f'Dog name: {self._name}\nDog Age: {self._age}' \
               f'\nDog species: {self.species}'


my_dog = Dog('Lucky', 5)
another_dog = Dog('Grey')
third_dog = Dog('A')
my_dog.birth_day()
print(my_dog.count_dogs)
print(f'Name: {my_dog.get_name()}, Age: {my_dog.get_age()}'
      f'\nName: {another_dog.get_name()}, Age: {another_dog.get_age()}')

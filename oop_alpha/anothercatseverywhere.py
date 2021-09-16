#!/usr/bin/python3


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around and is {self.age} years old'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Rufus(Cat):
    def sing(self, sounds):
        return f'{sounds}'


my_cats = [Simon('Simon', 5), Sally('Sally',
                                    7), Rufus('Rufus', 9)]

my_pets = Pets(my_cats)


my_pets.walk()

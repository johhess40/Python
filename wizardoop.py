#!/usr/bin/python3

class User:
    def sign_in(self):
        print('Youre logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}!')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows!: Number of arrows left- {self.num_arrows}')
wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 200)

for character in [wizard1, archer1]:
    character.attack()

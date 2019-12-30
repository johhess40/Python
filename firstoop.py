#!usr/bin/python3


class PlayerCharacter:
    #membership = True  # class object attribute

    def __init__(self, name, age, weapon):
        self.name = name
        self.age = age
        self.weapon = weapon

    def run(self):
        print(
            f'My name is {self.name} and I am {self.age}, and I am the master of {self.weapon}!')


player1 = PlayerCharacter("jimbo", 19, "Swords")
player2 = PlayerCharacter("steve", 22, "Wands")
player3 = PlayerCharacter("jeb", 44, "Mind Control")


print(player1.run())
print(player2.run())
print(player3.run())

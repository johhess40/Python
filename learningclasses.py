#!/usr/bin/python3
import json

class Mariokartplayer:
    def __init__(self, name, karttype):
        with open("mkcharacters.json") as mkd:
            stats = json.load)(mkd)
        self.name = name  # player character
        self.karttype = karttype  # kart selected
        self.score = 0  # current score
        self.item = None  # item character has picked up
        self.type = stats[name]["type"]
    def __str__(self):
        return self.name
# define a method called score

    def scorechange(self, condition):
        if condition == "coin":
            self.score += 10

        elif condition == "finishline":
            self.score += 100

        elif condition == "pushopponent":
            self.score += 25

        else:
            self.score += 5


def main():
    print("Learning about classes with Mario kart")
    player1 = Mariokartplayer("Yoshi", "50cc")

    print(player1.name)
    print(player1.karttype)
    print(player1.score)
    print(player1.item)

    # player1 just touched a coin
    player1.scorechange("coin")
    print(player1.score)
    player1.scorechange("finishline")
    print(player1.score)
    player1.scorechange("pushopponent")
    print(player1.score)
    print(player1.type)

if __name__ == "__main__":
    main()

# /usr/bin/python3
import json
import random


# open my poem database poems.json
# can do this with import json
# randomly select a poem from the pythonic data, use import.random
# print said poem to the screen
def main():

    with open("poems.json") as pj:
        pythonpoems = json.load(pj)  # convert json data to python data

    print(random.choice(list(pythonpoems.values())))


main()

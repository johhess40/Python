#!usr/bin/python3

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age



cat1 = Cat("uronomous", 109)
cat2 = Cat("death", 112)
cat3 = Cat("frodo", 400)

def get_oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

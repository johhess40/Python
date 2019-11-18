#!/usr/bin/env python3
user_input = input("Please enter your vendor name:")
user_input2 = input("Please enter your IPV4 address:")


## the lines below creates a single string that is passed to print()
# print("You told me the vendor name is:" + user_input)
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me your vendor name and IP are:"+ user_input, user_input2)
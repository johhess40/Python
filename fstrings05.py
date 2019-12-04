#!/usr/bin/python3

def main():
    myname = "John" #string
    myage = 29 #int
    mypets = ["Rowdy", "Sadie"] #list

    print(myname + " is the instructor")
    print(str(myage) + " is my age")
    print(myname, " is ", myage)
#f strings can be used anywhere
    print(f"My name, {myname} was given to me {myage} years ago")

    mystring = f"The name of my pets are {mypets[0]}, a labrador, and {mypets[1]} a rotweiller"

    print(mystring)
if __name__ == "__main__":
    main()

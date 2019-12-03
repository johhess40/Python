#!/usr/bin/python3

def main():
    mylist = []

    mylist.append("monday morning")

    mylist.append("tuesday evening")

    mylist.append("wednesday evening")

    mylist.append("thursday evening")

    print(mylist[0])

    print(mylist[2])

    studiomovies = {}

    studiomovies["pixar"] = ["toystory", "up"]

    studiomovies["universal"] = "JAWS", "super troopers"

    studiomovies["paramount"] = "Raiders of the Lost Ark", "king kong"

    print(studiomovies["paramount"][1])

    print(studiomovies["universal"][1])

    print(studiomovies["pixar"][1])


if __name__ == "__main__":
    main()

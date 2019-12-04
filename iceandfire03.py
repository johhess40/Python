#!/usr/bin/python3

import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters"


def main():
    # Ask user for input
    got_charToLookup = input("What is the name of the character we should lookup? ")

    # Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + "?name=" + got_charToLookup)

    # Decode the response
    got_dj = gotresp.json()


    print(f"The character {got_charToLookup} has the URL: {got_dj[0]['url']}")
    print(f"The character {got_charToLookup} has the alias: {got_dj[0]['aliases']}")
    print(f"The character {got_charToLookup} is played by: {got_dj[0]['playedBy']}")



main()

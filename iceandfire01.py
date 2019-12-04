#!/usr/bin/pytho3

import requests

AOIF = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)

    ##Decode the response
    got_dj = gotresp.json()

    ##print the response
    print(got_dj)
if __name__ == "__main__":
    main()

#!/usr/bin/python3
import pprint
import requests


POKEMONAPI = "https://pokeapi.co/api/v2/pokemon/mewtwo/"

def main():
    poke = requests.get(POKEMONAPI)

    pokejson = poke.json()

    #pprint.pprint(pokejson["abilities"])

    #for abl in pokejson["species"]:
        #print(abl)
    print(f'{pokejson["species"]["name"]} can be looked up at {pokejson["species"]["url"]}')
    print("Mewtwo appears in the following games")
    print("********")
    for abl in pokejson["game_indices"]:
        pprint.pprint(abl["version"]["name"])

    print("********")

    



if __name__ == "__main__":
    main()

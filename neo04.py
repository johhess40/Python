#!/usr/bin/python3

import json

import urllib.request

NEO = "https://api.nasa.gov/neo/rest/v1/feed?api_key="


def main():
    with open(r"/home/john/mycode/mycreds.txt", "r") as nc:
        myapikey = nc.read().rstrip("\n")

        print("****")

        print(myapikey)

        print("******")

        myneo = urllib.request.urlopen(NEO + myapikey)

        # make a request to NEO and save resp as neojson, bytes are returned
        neojson = myneo.read().decode("utf-8")

        neopy = json.loads(neojson)

        for astroids in neopy["near_earth_objects"]["2019-12-08"]:
            print("The Human name is: ", astroids["name"])
            print("The Astronomical ID is: ", astroids["id"])
            print("The estimated diameter is: ",
                  astroids["estimated_diameter"]["kilometers"])
            print("This asteroid is traveling at a miles per hour speed of: ",
                  astroids["close_approach_data"][0]["relative_velocity"]["miles_per_hour"])
            print()


if __name__ == "__main__":
    main()

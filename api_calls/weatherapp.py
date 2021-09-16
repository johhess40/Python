#!/usr/bin/python3

import requests

SEA_WTHR = "https://forecast.weather.gov/MapClick.php?lat=47.6036&lon=-122.3295&unit=0&lg=english&FcstType=text&TextType=1/api"

def main():
    sea_weatherTolookup = input("What are you interested in?: ")

    gotresp = requests.get(SEA_WTHR + "?name=" + sea_weatherTolookup)

    got_wt = gotresp.json()

    print(got_wt)

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)


    ciscodf.to_json("combined_ciscodata.json", orient="records")
    # exported to to_json

    ciscodf.to_csv("combined_ciscodata.csv", index=False)
    # exported to to_csv

    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    # exported to excel

    x = ciscodf.to_dict()
    print(x)



if __name__ == "__main__":
    main()

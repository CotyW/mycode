#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
   ###### ##Name and Aliases####
        name = got_dj.get('name', 'alias')
        alias = got_dj.get('aliases', 'no alias')

        if name:
            print(f"Name:{name}")
        elif aliases:
            print(f"Alias:{alias}")
        else:
            print("A girl has no name")


#######Houses #####
        house = got_dj.get('allegiances', [])
        print(house)

if __name__ == "__main__":
        main()


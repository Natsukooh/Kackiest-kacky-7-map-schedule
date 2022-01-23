#!/usr/bin/python3


import sys
import requests
import re


def main():
    
    if len(sys.argv) < 2:
        print("At least one argument required.")
        exit(1)

    try:
        map_numbers = list(map(int, sys.argv[1:]))
    except:
        print("Error : at least one argument failed to be parsed to an int. Exiting.")
        exit(1)

    data = []
    
    for map_number in map_numbers:
        request = requests.post("https://kacky.dingens.me/", data={"map": map_number})
        html = request.text

        time_search = re.search('juke = now \+ parseInt\(([0-9]+)\) \* 3600000 \+ parseInt\(([0-9]+)\) \* 60000;', html)
        if time_search:
            hours = time_search.group(1)
            minutes = time_search.group(2)
            data.append((map_number, int(hours), int(minutes)))
        else:
            print(f"Error finding time remaining for map {map_number}.")

    data.sort(key=lambda element: element[1] + element[2]/60)
    
    for entry in data:
        print(f"Map {entry[0]} will be played in {entry[1] if entry[1] != 0 else ''}{'h' if entry[1] != 0 else ''}{entry[2]}m")


main()
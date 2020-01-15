#!/usr/bin/python3
"""
search string in stars wars api
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'search': sys.argv[1]}
    url = 'https://swapi.co/api/people'
    r = requests.get(url, params=payload)
    rjson = r.json()
    count = rjson['count']
    people = rjson['results']
    print("Number of results: {}".format(count))
    if count:
        for person in people:
            print(person['name'])

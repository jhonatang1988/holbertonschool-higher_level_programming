#!/usr/bin/python3
"""
get id from github api
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2]))
    if r.status_code == 200:
        rjson = r.json()
        if rjson:
            print(rjson.get('id'))
        else:
            print("None")

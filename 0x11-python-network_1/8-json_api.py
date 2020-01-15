#!/usr/bin/python3
"""
sends a post with a letter as parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        rjson = r.json()
        if not rjson:
            print("No result")
        else:
            print("[{}] {}".format(rjson.get('id'), rjson['name']))
    except ValueError as e:
            print("Not a valid JSON")

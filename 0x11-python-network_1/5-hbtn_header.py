#!/usr/bin/python3
"""
get cystom header from request
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['x-Request-Id'])

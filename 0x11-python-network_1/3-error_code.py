#!/usr/bin/python3
"""
deals with errors in urllib request
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            html = res.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

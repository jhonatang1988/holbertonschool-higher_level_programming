#!/usr/bin/python3
"""
request an url and display custom header tag
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            with urllib.request.urlopen(sys.argv[1]) as res:
                header = res.info()['X-Request-Id']
                print(header)
        except urllib.error.URLError as e:
            print(e.reason)

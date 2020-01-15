#!/usr/bin/python3
"""
sends an email to url
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        values = {'email': sys.argv[2]}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as res:
            html = res.read().decode('utf-8')
            print(html)
    except urllib.error.URLError as e:
        print(e.reason)

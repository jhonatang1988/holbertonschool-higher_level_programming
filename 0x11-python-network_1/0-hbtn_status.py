#!/usr/bin/python3
"""
script that fetches and url with urllib
"""
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
            html = res.read()
            utfdecode = html.decode('utf-8')
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}"
                  .format(utfdecode))
    except urllib.error.URLError as e:
        print(e.reason)

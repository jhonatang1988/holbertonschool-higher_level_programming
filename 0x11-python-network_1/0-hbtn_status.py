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
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}"
                  .format('OK' if 'utf-8'
                  in res.info()['Content-Type'] else 'NO'))
    except urllib.error.URLError as e:
        print(e.reason)

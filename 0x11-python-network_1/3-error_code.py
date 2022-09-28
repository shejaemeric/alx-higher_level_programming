#!/usr/bin/python3
""" connect using urllib package"""

import urllib.request
import sys

if __name__ == "__main__":

    req = sys.argv
    try:
        with urllib.request.urlopen(req[1]) as response:
            out = response.read()
            print(out.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


#!/usr/bin/python3
""" connect using urllib package"""

import urllib.request
import sys

if __name__ == "__main__":

    req = sys.argv
    with urllib.request.urlopen(req[1]) as response:
        out = response.getheader('X-Request-Id')
        print(out)

#!/usr/bin/python3
""" connect using urllib package"""

import urllib.request
import sys

if __name__ == "__main__":

    req = sys.argv
    data = urllib.parse.urlencode({'email': req[2]})
    data = data.encode('ascii')
    url = urllib.request.Request(req[1], data)
    with urllib.request.urlopen(url) as response:
        out = response.read()
        print(out.decode('utf-8'))

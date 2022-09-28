#!/usr/bin/python3
""" connect using urllib package"""

import urllib.request

if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(req) as response:
        out = response.read()
        res = "Body response:\n\t- type: {}"
        res2 = "\t- content: {}\n\t- utf8 content: {}"
        print(res.format(type(out)))
        print(res2.format(out, out.decode('utf-8')))

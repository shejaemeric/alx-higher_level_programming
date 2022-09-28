#!/usr/bin/python3
""" connect using urllib package"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        out = response.read()
        res = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
        print(res.format(type(out), out, out.decode('utf-8')))

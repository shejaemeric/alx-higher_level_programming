#!/usr/bin/python3
""" connect using urllib package"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        line = response.readline()
        while (line):
            print("- {}".format(line))
            line = response.readline()

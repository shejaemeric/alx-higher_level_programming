#!/usr/bin/python3
"""connect and fetch using requests library and get X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    req = sys.argv
    res = requests.get(req[1]).headers.get("X-Request-Id")

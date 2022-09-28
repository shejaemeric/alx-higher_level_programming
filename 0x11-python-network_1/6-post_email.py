#!/usr/bin/python3
"""connect and fetch using requests library and get X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    url = (sys.argv) [1]
    param = {'email': (sys.argv) [2]}
    print(requests.get(url,param).content)

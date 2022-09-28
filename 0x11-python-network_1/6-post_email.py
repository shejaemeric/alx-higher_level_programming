#!/usr/bin/python3
"""connect and fetch using requests library and get X-Request-Id"""

import requests
from sys import argv

if __name__ == "__main__":
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)

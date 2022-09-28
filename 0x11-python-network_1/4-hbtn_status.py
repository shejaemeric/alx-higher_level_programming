#!/usr/bin/python3
# connect and fetch using requests library

from urllib import request
import requests

if __name__ == "__main__":
    req = "https://alx-intranet.hbtn.io/status"
    res = requests.get(req)
    o = "Body response:\n\t- type: {}\n\t- content: {}"
    print(o.format(type(res.content), res.content))

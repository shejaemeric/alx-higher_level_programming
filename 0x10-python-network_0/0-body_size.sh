#!/usr/bin/bash
#takes in a URL, sends a request to that URL,
#and displays the size of response

curl -i -s $1 | grep "Content-Length" | cut -d " " -f2

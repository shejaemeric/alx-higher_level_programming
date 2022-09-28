#!/bin/bash
#takes in a URL, sends a request to that URL n.
curl -i -s $1 | grep "Content-Length" | cut -d " " -f2

#!/bin/bash
#displays all HTTP methods the server will accept.
CURL -sX OPTIONS "$1"

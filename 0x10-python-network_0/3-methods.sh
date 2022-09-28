#!/bin/bash
#displays all HTTP methods the server will accept.
curl -sXL OPTIONS "$1"

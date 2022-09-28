#!/bin/bash
#GET request to the URL, and displays the body of the response
curl -si -d "X-School-User-Id=98" "$1"

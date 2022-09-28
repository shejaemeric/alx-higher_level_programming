#!/bin/bash
#GET request to the URL, and displays the body of the response
curl -si -H "X-School-User-Id=98" "$1"

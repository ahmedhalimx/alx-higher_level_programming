#!/bin/bash
# script asends a request to a URL to display the body size of the request.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2

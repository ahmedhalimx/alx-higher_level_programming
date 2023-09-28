#!/bin/env bash 
# script that sends a request to a given URL and displays the status of the response.
curl -s -L -X HEAD -w "%{http_code}" "$1"

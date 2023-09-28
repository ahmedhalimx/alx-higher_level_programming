#!/bin/bash
# script that accepts a URL and displays all HTTP methods acceptable by the server
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "

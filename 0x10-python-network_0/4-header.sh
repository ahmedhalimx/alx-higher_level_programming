#!/bin/bash
# script that accepts a given URL sends a GET request to the URL, displaying the body of the response
curl -s "$1" -H "X-School-User-Id: 98"

#!/bin/bash
# script that accepts a URL, sends a POST request to that URL,
# and displays the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"

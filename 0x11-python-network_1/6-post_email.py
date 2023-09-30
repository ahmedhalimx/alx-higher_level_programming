#!/usr/bin/python3
"""
script that sends a POST request to a given URL with a given email.
"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    responce = requests.post(sys.argv[1], data=email)
    print(responce.text)

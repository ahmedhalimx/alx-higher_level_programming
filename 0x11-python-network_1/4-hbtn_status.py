#!/usr/bin/python3
"""
script that fetches an URL
"""
import requests


if __name__ == "__main__":
    request = requests.get('https://alx-intranet.hbtn.io/status')
    t = request.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))

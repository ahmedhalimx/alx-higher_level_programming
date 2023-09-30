#!/usr/bin/pyhton3
"""
script that sends a POST request to a given URL with a given email.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    email = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, email)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

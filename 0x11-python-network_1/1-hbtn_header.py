#!/usr/bin/python3
"""
script that sends a POST request to the given URL
recives the email as a parameter and displays the
body of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    html = urllib.request.Request(url)
    with urllib.request.urlopen(html) as response:
        print(dict(response.headers).get("X-Request-Id"))

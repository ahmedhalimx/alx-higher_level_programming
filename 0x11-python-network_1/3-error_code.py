#!/usr/bin/python3
"""
A script sends a request to a given URL
displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as responce:
            print(responce.read().decode('UTF-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)

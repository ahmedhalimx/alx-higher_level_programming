#!/usr/bin/python3
"""
script that sends POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    user = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=user)
    try:
        json_fmt = response.json()
        if json_fmt == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_fmt.get("id"), json_fmt.get("name")))
    except ValueError:
        print("Not a valid JSON")

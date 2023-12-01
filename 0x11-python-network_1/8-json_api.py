#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    data = {"q": q}
    res = requests.post(url, data=data)
    try:
        body = res.json()
        if body == {}:
            print("No result")
        else:
            print("[{}] {}".format(body.get("id"), body.get("name")))
    except ValueError:
        print("Not a valid JSON")

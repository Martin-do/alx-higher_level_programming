#!/usr/bin/python3
"""script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {
        "email": sys.argv[2]
    }
    data = urllib.parse.urlencode(data).encode("ascii")
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)

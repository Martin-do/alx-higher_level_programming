#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    st_code = res.status_code
    if st_code >= 400:
        print("Error code: {}".format(st_code))
    else:
        print(res.text)

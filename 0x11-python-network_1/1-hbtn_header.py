#!/usr/bin/python3
"""sends a request to a url
and displays the value of the X-Request-Id
variable found in the response"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])

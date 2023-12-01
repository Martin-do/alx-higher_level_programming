#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    body = res
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

#!/usr/bin/python3
"""Displays the value of X-Request-Id in the response header of a URL"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))

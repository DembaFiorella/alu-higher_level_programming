#!/usr/bin/python3
"""Sends a POST request with an email parameter."""
import sys
import urllib.request
import urllib.parse

email = sys.argv[2]
data = urllib.parse.urlencode({"email": email}).encode("utf-8")

with urllib.request.urlopen(sys.argv[1], data=data) as response:
    print(response.read().decode("utf-8"))

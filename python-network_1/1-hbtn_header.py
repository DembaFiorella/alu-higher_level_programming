#!/usr/bin/python3
"""Fetches the X-Request-Id header value."""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))

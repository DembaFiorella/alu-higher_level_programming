#!/usr/bin/python3
"""Fetches the X-Request-Id header value."""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))

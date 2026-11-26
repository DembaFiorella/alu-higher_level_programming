#!/bin/bash
# Sends a GET request to a URL, follows redirects, and displays the body of a 200 response
curl -sfL "$1"

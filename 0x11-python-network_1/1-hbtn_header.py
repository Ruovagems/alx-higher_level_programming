#!/usr/bin/python3
"""
This script takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./fetch_request_id.py <URL>")

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.info().get('X-Request-Id')
            print(x_request_id)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)

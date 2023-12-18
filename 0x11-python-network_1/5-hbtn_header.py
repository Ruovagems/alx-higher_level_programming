#!/usr/bin/python3
"""
This script takes a URL;
-sends a request
-displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
if len(sys.argv) != 2:
sys.exit("Usage: ./fetch_request_id.py <URL>")

url = sys.argv[1]

response = requests.get(url)
	x_request_id = response.headers.get('X-Request-Id')

print(x_request_id)

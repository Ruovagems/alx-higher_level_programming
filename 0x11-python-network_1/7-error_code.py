#!/usr/bin/python3
"""
This script takes a URL and an email address, sends a POST request, and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./post_email.py <URL> <email>")

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)

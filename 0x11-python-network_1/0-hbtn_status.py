#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)

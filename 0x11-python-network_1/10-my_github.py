#!/usr/bin/python3
"""
This script takes a letter, sends a POST request, and displays the result from http://0.0.0.0:5000/search_user.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

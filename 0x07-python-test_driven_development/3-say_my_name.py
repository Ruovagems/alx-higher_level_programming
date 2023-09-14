#!/usr/bin/python3
# 3-say_my_name.py

"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    print(f"My name is {first_name} {last_name}")

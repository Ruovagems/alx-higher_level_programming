#!/usr/bin/python3

def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")

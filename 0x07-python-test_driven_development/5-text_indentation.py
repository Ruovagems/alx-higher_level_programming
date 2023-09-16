#!/usr/bin/python3
# 5-text_indentation.py

"""Defines a text-indentation function."""

def text_indentation(text):
    """
    Prints a text with 1 new line after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading and trailing spaces

    # Loop through the characters in the text
    for char in text:
        if char in ['.', '?', ':']:
            print(char + "\n")  # Print the character followed by 1 new line
        else:
            print(char, end='')  # Print other characters without a newline

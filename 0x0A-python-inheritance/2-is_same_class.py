#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object with.

    Returns:
        True if the object is an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class

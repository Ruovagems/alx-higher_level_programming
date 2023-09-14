#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object with.

    Returns:
        True if the object is an instance of, or inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)

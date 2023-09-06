#!/usr/bin/python3
"""

This module includes a class that defines a Rectangle.

"""
class Rectangle:
	"""Class that defines a Rectsngle."""
    def __init__(self, width=0, height=0):
	""" Method that initializes the instance."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
	"""Method that returns the value of the width."""
        return self.__width

    @width.setter
    def width(self, value):
	"""Method that defines the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
	"""Method that returns the value of a height.""""
        return self.__height

    @height.setter
    def height(self, value):
	"""Method that defines the value of a height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

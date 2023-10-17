#!/usr/bin/python3
"""

<<<<<<< HEAD

This module includes a class that defines a Rectangle.
=======
This module is composed by a class that defines a Rectangle
>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570


"""


class Rectangle:
<<<<<<< HEAD
	"""Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
	""" Method that initializes the instance
	
	Args:
		width: width of the rectangle 
		height: height of the rectangle


	"""
=======
    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle


        """
>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
	"""Method that returns the value of the width


	Returns:
		width of the rectangle


	"""
=======
        """ method that returns the value of the width

        Returns:
            width of the rectangle


        """

>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
	"""Method that defines the width
	Args:
=======
        """ method that defines the width

        Args:
>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


<<<<<<< HEAD
	"""
=======
        """

>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
	"""Method that returns the value of a height
	Returns:
            height of the rectangle
	"""


=======
        """ method that returns the value of the height

        Returns:
            height of the rectangle


        """

>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
	"""Method that defines the value of a height
	Args:
            value: height

=======
        """ method that defines the height

        Args:
            value: height
>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
<<<<<<< HEAD
	"""
=======


        """

>>>>>>> d4ab465574e84cb335e585997c34c0b8f0a47570
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

#!/usr/bin/python3
""" Define a  Rectangle class"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width (int): integer width
            height (int): integer height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: returns width
        Args:
            width (int): integer width
        Returns:
            rectangle width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """height: returns height
        Args:
            height (int): integer height
        Returns:
            rectangle height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ area: calculates area of rectangle
        Returns: returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter: calculates perimeter of rectangle
        Returns: returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation of rectangle
        Returns:
            string representation of rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height - 1):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        string += "#" * self.__width
        return string

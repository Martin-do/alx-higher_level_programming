#!/usr/bin/python3
""" Define a  Rectangle class"""


class Rectangle:
    """a rectangle object
    Attributes:
        number_of_instances (int): number of rectangle instances
        print_symbol (str): prints the symbol "#"
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ method.
        Args:
            width (int): integer width
            height (int): integer height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks which rectangle is bigger based on area
        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2
        Returns:
            returns bigger rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """creates a new rectangle of equal width and height
        Args:
            size (int): dimension of new rectangle
        Returns:
            returns a new rectangle with height=width=size
        """
        return cls(size, size)

    def __str__(self):
        """String representation of rectangle
        Returns:
            string representation of rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.height - 1):
            for j in range(self.width):
                string += str(self.print_symbol)
            string += "\n"
        string += str(self.print_symbol) * self.width
        return string

    def __repr__(self):
        """String representation of a rectangle object"""
        return ("Rectangle ({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Outputs a message when a rectangle instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

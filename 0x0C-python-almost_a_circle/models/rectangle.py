#!/usr/bin/python3
"""Define a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class

    Args:
        Base (Base): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method for Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): The x coord of the rectangle. Defaults to 0.
            y (int): The y coord of the rectangle. Defaults to 0.
            id (int): id attribute. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super.__init__(id)

    @property
    def width(self):
        """sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Args:
            value (int): value of the coord

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.x = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle

        Args:
            value (int): value of the coord

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.x = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coord of the rectangle

        Returns:
            int: the x coord
        """
        return self.x

    @x.setter
    def x(self, value):
        """sets the x coord of the rectangle

        Args:
            value (int): value of the coord

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.x = value

    @property
    def y(self):
        """get the x coord of the rectangle

        Returns:
            int: the x coord
        """
        return self.y

    @y.setter
    def y(self, value):
        """sets the y coord of the rectangle

        Args:
            value (int): value of the coord

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.y = value

    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: rectangle area
        """
        return self.width * self.height

    def display(self):
        """prints representation of rectangle"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns a particular string representation"""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """prints representation of rectangle"""
        for y in range(self.y):
            print("")
        for i in range(self.height):
            print(" "*self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """method that assigs argument to each attribute
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

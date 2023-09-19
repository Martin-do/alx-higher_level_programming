#!/usr/bin/python3
"""A Base class"""
import json
import turtle
import csv


class Base:
    """A Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for Base class

        Args:
            id (int): an id attribute. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep of
        list_dictionaries

        Args:
            list_dictionaries (dict): a dictionary

        Returns:
            JSON: JSON representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON str rep of list_objs to a file

        Args:
            list_objs (Obj): list of object instances
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a instantiated class from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dt) for dt in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        ijapa = turtle.Turtle()
        ijapa.screen.bgcolor("#b7312c")
        ijapa.pensize(3)
        ijapa.shape("turtle")

        for rect in list_rectangles:
            ijapa.showturtle()
            ijapa.up()
            ijapa.goto(rect.x, rect.y)
            ijapa.down()
            for i in range(2):
                ijapa.forward(rect.width)
                ijapa.left(90)
                ijapa.forward(rect.height)
                ijapa.left(90)
            ijapa.hideturtle()

        ijapa.color("#b5e3d8")
        for sq in list_squares:
            ijapa.showturtle()
            ijapa.up()
            ijapa.goto(sq.x, sq.y)
            ijapa.down()
            for i in range(2):
                ijapa.forward(sq.width)
                ijapa.left(90)
                ijapa.forward(sq.height)
                ijapa.left(90)
            ijapa.hideturtle()

        turtle.exitonclick()

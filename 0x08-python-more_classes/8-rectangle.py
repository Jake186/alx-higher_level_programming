#!/usr/bin/python3
"""Rectangle class to represent a square"""


class Rectangle():
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of rectangle
        Return:
        width of rectangle."""
        return self.__width

    @property
    def height(self):
        """ height of rectangle
        Return:
        height of rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter of the width
        Arguments:
        value: value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter of the width
        Arguments:
        value: value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle
        Return:
        area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of rectangle
        Return:
        perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ rectangle made using the character #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            if row < (self.__height - 1):
                string += (str(self.print_symbol) * self.__width) + "\n"
            else:
                string += (str(self.print_symbol) * self.__width)
        return string

    def __repr__(self):
        """ represent self for eval"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete self and count"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the largest rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return 

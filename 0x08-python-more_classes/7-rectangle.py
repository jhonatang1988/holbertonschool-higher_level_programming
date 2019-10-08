#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        for i in range(self.__height):
            for j in range(self.__width):
                print("{:s}".format(str(self.print_symbol)), end="")
            if not i == self.height - 1:
                print()
        return("")

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    @staticmethod
    def __del__():
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

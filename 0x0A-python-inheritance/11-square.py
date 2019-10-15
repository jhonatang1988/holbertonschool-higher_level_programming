#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Square - an square object.
"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return ("[{}] {}/{}".
                format(self.__class__.__name__, self.__size, self.__size))

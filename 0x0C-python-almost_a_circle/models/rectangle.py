#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, a_value):
        if type(a_value) is type(1):
            if a_value < 1:
                raise ValueError("width must be > 0")
            else:
                self.__width = a_value
        else:
            raise TypeError("width must be an integer")


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, a_value):
        if type(a_value) is type(1):
            if a_value < 1:
                raise ValueError("height must be > 0")
            else:
                self.__height = a_value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, a_value):
        if type(a_value) is type(1):
            if a_value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = a_value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, a_value):
        if type(a_value) is type(1):
            if a_value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = a_value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        return self.__width * self.__height

    def display(self):
        for a_y in range(self.__y):
            print()
        for a_height in range(self.__height):
            for a_x in range(self.__x):
                print(" ", end="")
            for a_width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}" \
              .format(self.id, self.__x, self.__y, \
                      self.__width, self.__height))

    def update(self, *args, **kwargs):
        if args:
            arg_names = list(self.__init__.__code__.co_varnames)
            del(arg_names[0])
            arg_names.insert(0, arg_names.pop())
            for index, value in enumerate(args):
                setattr(self, arg_names[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

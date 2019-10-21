#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self):
        self.__y = y

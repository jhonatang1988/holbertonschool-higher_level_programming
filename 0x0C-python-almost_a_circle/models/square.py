#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, a_value):
        Rectangle.width.fset(self, a_value)
        Rectangle.height.fset(self, a_value)

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

#!/usr/bin/python3
"""
Square Model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ method
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ method
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, a_value):
        """
        size setter
        """
        Rectangle.width.fset(self, a_value)
        Rectangle.height.fset(self, a_value)

    def update(self, *args, **kwargs):
        """
        update method
        """
        if args:
            arg_names = list(self.__init__.__code__.co_varnames)
            del(arg_names[0])
            arg_names.insert(0, arg_names.pop())
            for index, value in enumerate(args):
                setattr(self, arg_names[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        to_dictionary method
        """
        arg_names = list(self.__init__.__code__.co_varnames)
        del(arg_names[0])
        new_dict = {}
        for k in arg_names:
            new_dict[k] = getattr(self, k)
        return new_dict

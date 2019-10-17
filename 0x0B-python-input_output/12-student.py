#!/usr/bin/python3


class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            if type(attrs) is list:
                new_dict = {}
                for att in attrs:
                    if att in self.__dict__:
                        new_dict[att] = self.__dict__[att]
            return new_dict

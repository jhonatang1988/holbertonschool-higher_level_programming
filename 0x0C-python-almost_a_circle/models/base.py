#!/usr/bin/python3
"""
base class
"""
import json
import os


class Base():
    """
    class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string static method
        """
        if list_dictionaries is not None and list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """  save_to_fie: save in a fil the dicts of each instance passed"""
        filename = cls.__name__ + ".json"
        new = []
        result = ""
        with open(filename, 'w') as fd:
            if list_objs is None:
                result = cls.to_json_string(new)
            else:
                for elem in list_objs:
                    new.append(elem.to_dictionary())
                result = cls.to_json_string(new)
            fd.write(result)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string static method
        """
        if json_string and json_string is not None:
            return json.loads(json_string)
        return list()

    @classmethod
    def create(cls, **dictionary):
        """
        create class method
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file class method
        """
        filename = cls.__name__ + ".json"

        if os.path.isfile("./" + filename):
            new_list = list()
            with open(filename, encoding='utf-8', mode='r') as a_file:
                an_obj = a_file.read()
                a_list_of_dicts = cls.from_json_string(an_obj)
                for attrs in a_list_of_dicts:
                    new_list.append(cls.create(**attrs))
                return new_list
        else:
            return list()

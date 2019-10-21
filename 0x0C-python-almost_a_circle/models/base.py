#!/usr/bin/python3
import json
import os


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries is None and list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        a_list = []
        for obj in list_objs:
            a_list.append(obj.to_dictionary())
        json_dictionary = Base.to_json_string(a_list)
        filename = cls.__name__ + ".json"
        with open(filename, encoding='utf-8', mode='w') as a_file:
            return a_file.write(json_dictionary)

    @staticmethod
    def from_json_string(json_string):
        if json_string and not json_string is None:
            return json.loads(json_string)
        return list()

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
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

#!/usr/bin/python3
import json

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

#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename) as a_file:
        an_object = a_file.read()
        return(json.loads(an_object))

#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, encoding='utf-8', mode='a') as a_file:
        return a_file.write(text)

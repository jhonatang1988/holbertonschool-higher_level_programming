#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open('my_file_0.txt', encoding='utf-8') as a_file:
        for lines, l in enumerate(a_file):
            if lines < nb_lines or nb_lines <= 0:
                print("{}".format(l), end="")

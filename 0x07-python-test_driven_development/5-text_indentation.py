#!/usr/bin/python3
def text_indentation(text):
    flag = 0
    try:
        length = len(text)
        for i in text:
            if flag and i  is ' ':
                flag = 0
                continue
            print("{:s}".format(i), end="")
            if i is '.' or i is '?' or i is ':':
                flag = 1
                print()
                print()
    except TypeError:
        print("TypeError: text must be a string")

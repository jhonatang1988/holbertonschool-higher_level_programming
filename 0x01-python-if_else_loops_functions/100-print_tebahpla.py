#!/usr/bin/python3
for c in reversed(range(97, 123)):
    if (c % 2 != 0):
        c = chr(c - 32)
    else:
        c = chr(c)
    print("{}".format(c), end="")

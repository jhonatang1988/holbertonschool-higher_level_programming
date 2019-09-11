#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(1, 10):
        if (n1 < n2):
            if n1 != 8 or n2 != 9:
                print("{}{}".format(n1, n2), end=", ")
            else:
                print("{}{}".format(n1, n2))

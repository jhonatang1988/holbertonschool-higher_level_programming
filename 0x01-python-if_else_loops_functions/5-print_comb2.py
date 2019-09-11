#!/usr/bin/python3
for nn in range(0, 100):
    if nn != 99:
        print("{:02d}".format(nn), end=", ")
    else:
        print("{:02d}".format(nn))

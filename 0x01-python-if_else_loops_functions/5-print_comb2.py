#!/usr/bin/python3
for nn in range(0, 100):
    print("{:02d}".format(nn), end="")
    if nn != 99:
        print(",", end=" ")
print()

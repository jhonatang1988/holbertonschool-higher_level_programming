#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if(len(sys.argv) > 1):
        if len(sys.argv) == 2:
            print("{} argument:".format(len(sys.argv) - 1))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
        for a in sys.argv[1:]:
            print("{}: {}".format(sys.argv.index(a), a))
    else:
        print("0 arguments.")

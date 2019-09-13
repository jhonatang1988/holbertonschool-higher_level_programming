#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if(len(sys.argv) > 1):
        result = 0
        for a in sys.argv[1:]:
            result = result + int(a)
        print("{}".format(result))
    else:
        print("0")

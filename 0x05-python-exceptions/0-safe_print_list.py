#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for elems in my_list:
            i += 1
            if i <= x:
                print("{}".format(elems), end="")
        if x >= i:
            x = i
        print()
        return x
    except:
        print("unknown error hapenned")

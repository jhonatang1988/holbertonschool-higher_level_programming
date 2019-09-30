#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    flag = 0
    try:
        result = a / b
    except ZeroDivisionError:
        flag = 1
        pass
    except:
        print("unknown error")
    finally:
        if flag:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(result))
    if flag:
        return None
    else:
        return result

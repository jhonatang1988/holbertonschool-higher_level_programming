def safe_print_integer(value):
    try:
        i = int(value)
    except ValueError:
        return False
    else:
        print("{}".format(i))
        return True

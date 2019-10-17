def number_of_lines(filename=""):
    lines = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            lines += 1
    return lines

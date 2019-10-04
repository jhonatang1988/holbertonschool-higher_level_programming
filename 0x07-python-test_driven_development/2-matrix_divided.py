#!/usr/bin/python3
def matrix_divided(matrix, div):
    result = []
    result2 = []
    lengths = []
    if type(div) == type(1) or type(div) == 1.0:
        if int(div) == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    for x in matrix:
        lengths.append(len(x))
        if type(x) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if(len(set(lengths)) != 1):
        raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        for j in i:
            if not type(j) == type(1) and not type(j) == type(1.0):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            result.append(round(j / div, 2))
        result2.append(result)
        result = []
    return result2

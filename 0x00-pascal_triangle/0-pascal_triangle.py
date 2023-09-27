#!/usr/bin/python3
""" Funtion that representing the Pascal’s triangle """
def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal’s triangle of n
    """
    list = []
    for i in range(n):
        list.append([])
        list[i].append(1)
        j = 1
        while j < i:
            list[i].append(list[i - 1][j - 1] + list[i - 1][j])
            j += 1
        if(n != 0 and i > 0):
            list[i].append(1)
    return list

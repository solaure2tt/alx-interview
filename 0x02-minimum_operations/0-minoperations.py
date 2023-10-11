#!/usr/bin/python3
""" calculates the fewest number of operations needed to
    result in exactly n H characters in the file
"""


def minOperations(n):
    """minimum operations to copy and past n H
       args:
         n (int): Number of times to see H in a file
       return:
         a minimum number of operations to have n H or 0
    """
    result = 0
    div = 2
    while n > 1:
        while n % div == 0:
            result += div
            n /= div
        div += 1
    return result

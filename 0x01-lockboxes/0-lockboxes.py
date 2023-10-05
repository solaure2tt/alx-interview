#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """verify if every box will be open"""
    res = [0 for i in range(len(boxes))]
    res[0] = 1
    keys = boxes[0]
    k = 0
    while k < len(keys):
        val = keys[k]
        if val in range(len(res)) and res[val] == 0:
            res[val] = 1
            for i in range(len(boxes[val])):
                if boxes[val][i] not in keys:
                    keys.append(boxes[val][i])
        k = k + 1
    if res.count(0) > 0:
        return False
    else:
        return True

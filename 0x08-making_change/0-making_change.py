#!/usr/bin/python3
"""
   Given a pile of coins of different values,
   determine the fewest number of coins needed
   to meet a given amount total
"""
import sys


def makeChange(coins, total):
    """ given coins, method that determines the
        fewestnumber of coins needed to meet total
        Args:
          coins: list of infinite coins
          total: amount to meet
        Return:
          number of coins needs
    """
    length = len(coins)
    if total == 0:
        return 0
    res = sys.maxsize
    coins.sort(reverse=True)
    for i in range(0, length):
        if (coins[i] <= total):
            r = makeChange(coins, total - coins[i])
            if (r != sys.maxsize and r + 1 < res):
                res = r + 1
    return res

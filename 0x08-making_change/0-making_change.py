#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        while coin <= total:
            total -= coin
            num_coins += 1
        if total == 0:
            return num_coins

    return -1

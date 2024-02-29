#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount"""


def makeChange(coins, total):
    memo = {}

    def helper(total):
        if total < 0:
            return -1
        if total == 0:
            return 0
        if total in memo:
            return memo[total]

        min_coins = float('inf')
        for coin in coins:
            remaining = total - coin
            result = helper(remaining)
            if result >= 0:
                min_coins = min(min_coins, result + 1)

        memo[total] = min_coins if min_coins != float('inf') else -1
        return memo[total]

    return helper(total)

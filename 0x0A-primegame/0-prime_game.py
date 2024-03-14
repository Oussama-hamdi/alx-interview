#!/usr/bin/python3
"""Game of prime numbers"""


def is_prime(n):
    """Check if number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def isWinner(x, nums):
    """Determines the winner of the Prime Game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1 or (n % 2 == 0 and n != 2):
            maria_wins += 1
        elif is_prime(n):
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

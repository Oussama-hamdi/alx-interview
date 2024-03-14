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

    for num_limit in nums:
        primes_available = sum(
                1 for num in range(1, num_limit + 1) if is_prime(num))
        if primes_available % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

#!/usr/bin/python3

"""This module contains functions to determine who the winner of
each game is in a prime number game"""


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False
    for start in range(2, int(max_n ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                is_prime[multiple] = False

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Step 2: Determine the winner for each game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

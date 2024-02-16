#!/usr/bin/python3
def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        if n == 1:
            return False
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        # Maria wins if the number of primes is even, otherwise Ben wins
        return len(primes) % 2 == 0

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
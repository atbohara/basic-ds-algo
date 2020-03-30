"""Generate a list of prime numbers up to a given max.
Uses The Sieve of Eratosthenes, which is a concept to generate
such list efficiently.
"""

import math


def get_prime_list(N):
    """Returns a list of prime numbers smaller or equal to N."""
    flags = [1] * (N+1) # flags[i] would be 1 if i is prime.
    flags[0] = 0
    flags[1] = 0
    prime = 2
    while prime <= int(math.sqrt(N)):
        cross_off(flags, prime)
        prime = get_next_prime(flags, prime)
    primes = [i for i, x in enumerate(flags) if x]
    return primes


def cross_off(flags, prime):
    """Disables all the indices corresponding to the remaining multipliers
    of prime. We can start this check from prime * prime,
    becuase values smaller than that would have already been checked.
    E.g., if prime is 4, then 4*2 and 4*3 would have been covered when
    this fucntion was called with prime = 2 and prime = 3, respectively.
    """
    for i in range(prime*prime, len(flags), prime):
        flags[i] = 0


def get_next_prime(flags, prime):
    """Returns the index in flags that is set and greater than prime."""
    next = prime + 1
    while (next<len(flags)) and (not flags[next]):
        next += 1
    return next


if __name__=='__main__':
    n = int(input())
    print(get_prime_list(n))

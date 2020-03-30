"""Check if a given number is prime."""

import math


def is_prime(number):
    """Returns True if the given number is prime."""
    if number < 2:
        return False
    sqrt = int(math.sqrt(number))
    for i in range(2, sqrt+1):
        if not (number%i):
            return False
    return True


if __name__ == '__main__':
    x = int(input())
    print(is_prime(x))

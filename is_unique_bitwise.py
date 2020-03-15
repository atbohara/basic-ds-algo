"""Algorithms to find whether all the chracters in a given string are unique.
Assumption: only lowercase alphabet. (Can be generalized.)
Time: O(n)
Space: O(1)
"""
def is_unique_bitwise(word):
    """Returns True if all the characters in word are unique.
    Uses single integer and bitwise operations to improve space utilization and speed.
    """
    checker = 0
    for ch in word:
        val = ord(ch) - ord('a')
        if (checker & (1 << val)):
            return False
        checker |= (1 << val)
    return True

if __name__ == "__main__":
    word = 'university'
    print(word)
    print(is_unique_bitwise(word))
    word = 'isolate'
    print(word)
    print(is_unique_bitwise(word))

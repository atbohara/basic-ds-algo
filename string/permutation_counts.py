"""Method to find whether given two strings are permutations of each other.

Solution by counting different characters in each string.

Time: O(n) # Sorts two strings, not optimal.
Space: O(1)
"""

from collections import defaultdict


def check_permutation(word1, word2):
    """Returns True if word2 is a permutation of word1"""
    if len(word1) != len(word2):
        return False
    char_counts = defaultdict(int) # We are using a hash table
    for ch in word1:
        char_counts[ch] += 1
    for ch in word2:
        char_counts[ch] -= 1
        if char_counts[ch] < 0:
            return False
    return True


if __name__ == '__main__':
    word1 = 'doodle'
    word2 = 'leddoo'
    print('word1: %s, word2: %s' %(word1, word2))
    print(check_permutation(word1, word2))
    print()

    word1 = 'univ'
    word2 = 'deni'
    print('word1: %s, word2: %s' %(word1, word2))
    print(check_permutation(word1, word2))
    print()

    word1 = '!@#$'
    word2 = '$#@!'
    print('word1: %s, word2: %s' %(word1, word2))
    print(check_permutation(word1, word2))

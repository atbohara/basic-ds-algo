"""Method to find whether given two strings are permutations of each other.

Solution by using sorting the strings.

Time: O(n logn) # Sorts two strings, not optimal.
Space: O(1)
"""


def check_permutation(word1, word2):
    """Returns True if word2 is permutation of word1"""
    if len(word1) != len(word2):
        return False
    return sorted(word1) == sorted(word2) # sorted() returns a list


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

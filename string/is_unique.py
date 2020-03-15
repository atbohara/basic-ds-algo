"""Algorithms to find whether all the chracters in a given string are unique.
Assumption: only ASCII characters.
Time: O(n)
Space: O(1)
"""

def is_unique_chars(word):
    """Returns True if all the characters in word are unique.
    """
    if len(word) > 128:
        return False
    found = set()
    for char in word:
        if char in found:
            return False
        found.add(char)
    return True

if __name__ == "__main__":
    word = 'university'
    print(word)
    print(is_unique_chars(word))
    word = 'isolate'
    print(word)
    print(is_unique_chars(word))

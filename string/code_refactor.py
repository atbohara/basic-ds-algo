"""Code refactor functionality using strings/lists.
Given a list of Replacement objects (metadata), modify a given text.
All the start indices in Replacement objects correspond to the original text.
"""

from collections import defaultdict


class Replacement:
    """Class to represent metadata."""
    def __init__(self, start, before, after):
        self.start = start
        self.before = before
        self.after = after

def get_dict(obj_list):
    """Returns a dict of form: {index: before_len, 'after'}
    """
    metadata = defaultdict(dict)
    for obj in obj_list:
        metadata[obj.start]['len'] = len(obj.before)
        metadata[obj.start]['after'] = obj.after
    return metadata

def refactor(code, replacements):
    """Returns refactored code; None if index out of bound."""
    metadata = get_dict(replacements) # O(R), R = number of Replacement objects
    for index in metadata: # O(R)
        if index >= len(code):
            return None
    new_code = []
    i = 0
    while i < len(code): # O(N), N = length of 'code'
        if i not in metadata:
            new_code.append(code[i])
            i += 1
            continue
        for ch in metadata[i]['after']: # O(A), A = length of 'after' words
            new_code.append(ch)
        i += metadata[i]['len']
    return ''.join(new_code)

def main():
    code = "This is source code!"
    print("Original code: %s" %code)
    replacements = [Replacement(0, 'This', 'That'), Replacement(5, 'is', 'are'), Replacement(19, '!', '??')]

    new_code = refactor(code, replacements)
    print("Refactored code: %s" %new_code)


if __name__ == '__main__':
    main()

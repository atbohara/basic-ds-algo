"""Rearrange node-pairs in a given linked list.
Demonstration of 'runner' technique.
"""

from linked_list import Node
from linked_list import LinkedList


def rearrange_pairs(orig_list):
    """Modifies the input list in-place.
    O(N).
    """
    slow_ptr = orig_list.head
    fast_ptr = orig_list.head
    while fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next # jumps two nodes every time
    # When the fast_ptr reaches end, put it back at head.
    # slow_ptr would be at (N/2)+1 element.
    fast_ptr = orig_list.head

    # Start 'weaving' the pairs.
    while slow_ptr:
        # Store the original next nodes in temp variables.
        next1 = slow_ptr.next
        next2 = fast_ptr.next
        # Rearrange pointers.
        fast_ptr.next = slow_ptr
        if not next1: # p1 reached the last node
            # Cleanup: remove unneccessary links (optional).
            slow_ptr = None
            fast_ptr = None
            next2 = None
            break
        slow_ptr.next = next2
        slow_ptr = next1
        fast_ptr = next2


def main():
    orig_items = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
    orig_list = LinkedList()
    for item in orig_items:
        orig_list.insert_at_tail(item)
    print("Original list:")
    orig_list.print()

    rearrange_pairs(orig_list)
    print("After rearranging:")
    orig_list.print()


if __name__ == '__main__':
    main()

"""Definitions of a singly linked list along with basic methods.
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_head(self, data):
        """Insert a new node with given data at the beginning of the list.
        O(1).
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert a new node with given data at the end of the list.
        O(N).
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def getLastandSize(self):
        """Returns the last(tail) node and the size (number of nodes).
        Returns (None, 0) for empty list.
        O(N).
        """
        if not self.head:
            return (None, 0)
        size = 1
        node = self.head
        while node.next:
            size += 1
            node = node.next
        return (node, size)

    def search(self, data):
        """Returns the reference to the first Node having the desired value.
        Returns None, if data was not present.
        O(N).
        """
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def delete(self, data):
        """Removes the first Node having the desired value.
        Returns head.
        O(N)
        """
        node = self.head
        if not node: # Empty list
            return None
        if node.data == data: # 'data' found at head
            return node.next

        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return self.head
            node = node.next
        return self.head


    def print(self):
        """O(N)"""
        if not self.head:
            print("Empty list")
            return
        node = self.head
        repr = str(node.data)
        while node.next:
            node = node.next
            repr += ' -> %s' %(node.data)
        print(repr)

    def get_node_at_index(self, index):
        """Returns the reference to the Node appearing at the given index.
        Indices start at 0, as usual.
        Returns None if the list is empty or the desired index out of bound.
        O(N).
        """
        if not self.head:
            return None
        node = self.head
        while (index > 0) and (node):
            node = node.next
            index -= 1
        return node

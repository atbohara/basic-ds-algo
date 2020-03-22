"""Test cases for the basic functionality of linked list."""

from linked_list import Node
from linked_list import LinkedList

if __name__ == '__main__':
    my_list = LinkedList()
    print("Printing an empty list and its size")
    my_list.print()
    print(my_list.getLastandSize()[1])
    print()

    print("Insert the first node, print the size of the list")
    my_list.insert_at_tail(1)
    print(my_list.getLastandSize()[1])
    print()

    print("Insert a few more nodes, print the size and content of the list")
    my_list.insert_at_tail(2)
    my_list.insert_at_tail(3)
    my_list.insert_at_tail(4)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Insert a node at head, and check size, content")
    my_list.insert_at_head(0)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Search a node with data")
    search_term = 0
    print("Found %d" %search_term if my_list.search(search_term) else "Not found %d" %search_term)
    search_term = 6
    print("Found %d" %search_term if my_list.search(search_term) else "Not found %d" %search_term)
    print()

    print("Delete an intermediate node, and check size, content")
    my_list.head = my_list.delete(1)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Delete the head node, and check size, content")
    my_list.head = my_list.delete(0)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Delete the last node, and check size, content")
    my_list.head = my_list.delete(4)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Again, delete the last node, and check size, content")
    my_list.head = my_list.delete(3)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("One more time")
    my_list.head = my_list.delete(2)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Finally, with the empty list")
    my_list.head = my_list.delete(2)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    print("Re-insert some nodes, print the size and content of the list")
    my_list.insert_at_tail(1)
    my_list.insert_at_tail(2)
    my_list.insert_at_tail(3)
    my_list.insert_at_tail(4)
    print(my_list.getLastandSize()[1])
    my_list.print()
    print()

    index = 0
    print("Node at index %d has value: %d\n" %(index, my_list.get_node_at_index(index).data))
    index = 2
    print("Node at index %d has value: %d\n" %(index, my_list.get_node_at_index(index).data))
    index = 3
    print("Node at index %d has value: %d\n" %(index, my_list.get_node_at_index(index).data))
    print("Both tail and size")
    (last, size) = my_list.getLastandSize()
    print(last.data, size)

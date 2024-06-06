# Given the head of a singly linked list, write a method to return the middle
# node fo the linked list. If the total number of nodes in the linked list is
# even, return the second middle node.

from linked_list import Node, linked_list_middle


if __name__ == "__main__":
    Head = Node(1)
    Second = Node(2)
    Third = Node(3)
    Fourth = Node(4)
    Fifth = Node(5)
    Sixth = Node(6)
    Seventh = Node(7)

    Head.next = Second
    Second.next = Third
    Third.next = Fourth
    Fourth.next = Fifth

    print(f"The middle value of the list is: {linked_list_middle(Head).value}")

    Fifth.next = Sixth
    Sixth.next = Seventh
    print(f"The middle value of the list is: {linked_list_middle(Head).value}")

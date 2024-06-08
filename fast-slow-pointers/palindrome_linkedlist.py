# Given the head of a singly linked list, write a methor to check if the linked
# list is a palindrome or not
# The algorithm should use constant space and the input linked list should be
# in the original form once the algorithm is finished. The algorithm should have
# O(N) time complexity, where 'N' is the number of nodes in the linked list

from linked_list import Node, is_palindrome, linked_list_middle, reverse_linked_list


if __name__ == "__main__":
    Head = Node(1)
    Second = Node(2)
    Third = Node(3)
    Fourth = Node(2)
    Fifth = Node(1)

    Head.next = Second
    Second.next = Third
    Third.next = Fourth
    Fourth.next = Fifth

    print("Linked list values:")

    current = Head

    while current:
        print(current.value)
        current = current.next

    print("Linked list middle node:", linked_list_middle(Head).value)
    # print("Linked list last node:", reverse_linked_list(Head).value)
    print("Is the linked list a palindrome:", is_palindrome(Head))

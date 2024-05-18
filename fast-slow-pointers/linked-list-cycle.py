from linked_list import Node, has_cycle

# given the head of a singly-linked list, write a function to determine if the
# linkedlist has a cycle in it or not
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    head.next = second
    second.next = third
    third.next = fourth

    print(head.next.value)
    print(second.next.value)
    print(third.next.value)

    fourth.next = second

    print(has_cycle(head))

    fourth.next = second
    print(has_cycle(head))

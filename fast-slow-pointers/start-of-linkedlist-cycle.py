# Given the head of a Singly LinkedList that contains a cycle, write a function
# to find the starting node of the cycle.
from linked_list import Node, find_cycle_start, has_cycle

head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = None

sample_1 = find_cycle_start(head)

print("linked list has cycle:", str(True if has_cycle(head) else False))
print(
    "the meeting point value is:",
    str(find_cycle_start(head).value) if sample_1 else "None",
)

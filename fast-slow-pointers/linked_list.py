class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False
        return None

    slow = head
    fast = head.next
    fast = head

    while fast != slow:
        if not fast or not fast.next:
            return False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return True
    return None


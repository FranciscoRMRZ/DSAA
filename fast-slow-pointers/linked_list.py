class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast != slow:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

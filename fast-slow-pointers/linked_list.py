class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return None


def find_cycle_start(head):
    meeting_point = has_cycle(head)

    if not meeting_point:
        return None

    slow = head
    fast = meeting_point

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return meeting_point

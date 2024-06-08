class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node) -> Node | None:
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


def linked_list_middle(head):
    # Initialize slow and fast pointers
    slow, fast = head, head

    # Run a loop to find the list end
    # Since the fast pointer walks at double the speed of the slow poiinter
    # by the time the end of the list is reaches, the slow pointer should
    # be at the middle of  the list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Return the slow pointer
    return slow


def reverse_linked_list(head: Node) -> Node:
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous

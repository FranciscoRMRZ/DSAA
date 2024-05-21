# Any number will be called a happy number if, after repeatedly replacing it
# with a number equal to the sum of the square of all of its digits, leads us
# to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
# they will be stuck in a cycle of numbers which does not include ‘1’.


def get_next(num: int) -> bool:
    return sum(int(char) ** 2 for char in str(num))


# This implementation uses memoization to detect if the process entered a loop
def is_happy_number(n: int) -> bool:
    seen_numbers = set()

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next(n)

    return n == 1


# This implementation uses Floyd's Tortoise and Hare two-pointer algorithm
def is_happy_number_tp(n: int) -> bool:
    slow, fast = n, n
    while True:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        if slow == fast:
            return False
    return slow == 1

# Given two strings containing backspaces (identified by the character ‘#’),
# check if the two strings are equal


def remove_backpaces(word: str) -> str:
    stack = []
    for char in word:
        if char != "#":
            stack.append(char)
        elif stack:
            stack.pop()

    return "".join(stack)


def compare_strings(str1: str, str2: str) -> bool:
    return remove_backpaces(str1) == remove_backpaces(str2)


if __name__ == "__main__":
    sample_1 = "xy#z"
    sample_2 = "xzz#"
    sample_3 = "xywrrmp"
    sample_4 = "xywrrmu#p"

    print("Remove backspaces from sample_1:", sample_1)
    print("Result:", remove_backpaces(sample_1))
    print("Remove backspaces from sample_2:", sample_2)
    print("Result:", remove_backpaces(sample_2))
    print(
        "Are sample_1 and sample_2 equal after backspace removal?:",
        compare_strings(sample_1, sample_2),
    )

    print("Remove backspaces from sample_3:", sample_3)
    print("Result:", remove_backpaces(sample_3))
    print("Remove backspaces from sample_4:", sample_4)
    print("Result:", remove_backpaces(sample_4))
    print(
        "Are sample_1 and sample_2 equal after backspace removal?:",
        compare_strings(sample_3, sample_4),
    )

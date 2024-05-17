# given an array, find the length of the smallest subarray in it which when
# sorted will sort the whole array
from typing import List


def min_sort_subarray(arr: List) -> int:
    n = len(arr)

    # find the first out of order element from the left
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # if no out of order element exists, the array was already sorted
    if left == n - 1:
        return 0

    # find the first out of order element from the right
    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    # determine the min and max values within the subarray
    subarray_min = min(arr[left : right + 1])
    subarray_max = max(arr[left : right + 1])

    # expand the subarray to the left
    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1

    # expand the subarray to the right
    while right < n - 1 and arr[right + 1] < subarray_max:
        right += 1

    return right - left + 1


if __name__ == "__main__":
    sample_1 = [1, 2, 5, 3, 7, 10, 9, 12]
    sample_2 = [1, 3, 2, 0, -1, 7, 10]
    sample_3 = [1, 2, 3]
    sample_4 = [3, 2, 1]

    print("sample_1:", min_sort_subarray(sample_1))
    print("sample_2:", min_sort_subarray(sample_2))
    print("sample_3:", min_sort_subarray(sample_3))
    print("sample_4:", min_sort_subarray(sample_4))

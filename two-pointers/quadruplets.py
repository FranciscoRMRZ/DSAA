# Given an array of unsorted numbers and a target number, find all unique
# quadruplets in it, whose sum is equal to the target number.
def find_quadruplets(nums: list, target: int) -> list:
    quadruplets = []
    # find target sum with two numbers
    # TODO: find target sum with three numbers
    # TODO: find target sum with four numbers

    left = 0
    right = len(nums) - 1
    sorted_nums = sorted(nums)

    while left < right:
        if sorted_nums[left] + sorted_nums[right] < target:
            left += 1
        if sorted_nums[left] + sorted_nums[right] == target:
            quadruplets.append([sorted_nums[left], sorted_nums[right]])
            left += 1
            right -= 1
        else:
            right -= 1

    return quadruplets

if __name__ == "__main__":
    sample_1 = ([4,1,2,-1,1,-3], 1)
    sample_2 = ([2, 0, -1, 1, -2, 2], 2)
    print('Sample 1:', sample_1)
    print('Find pairs equal to target in sample_1:', find_quadruplets(*sample_1))
    print('sample_2:', sample_2)
    print('Find pairs equal to target in sample_1:', find_quadruplets(*sample_2))


# Given an array containing 0s, 1s and 2s, sort the array in-place. You should 
# treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s 
# to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; 
# and since our input array also consists of three different numbers that is 
# why it is called Dutch National Flag problem.
def sort_colors(nums):
    # initializa the pointers
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            # if the element is 0, swap mid and low elements and increase both 
            # pointers
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # if the element equals 1, increase the mid pointer 
            mid += 1
        else:
            # If ti is neither 0 or 1, swap the mid and high element, and increase
            # both pointers
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

if __name__ == "__main__":
    # Example usage:
    nums = [2, 0, 2, 1, 1, 0]
    print("Input array", nums)
    sorted_nums = sort_colors(nums)
    print("Sorted array:", sorted_nums)

# Given an array of unsorted numbers and a target number, find all unique
# quadruplets in it, whose sum is equal to the target number.
def find_quadruplets(nums: list, target: int) -> list:
    quadruplets = []
    nums.sort()
    n = len(nums)

    for j in range(n-3):
        # Avoid duplicates
        if j > 0 and nums[j] == nums[j-1]:
            continue

        for i in range(j+1, n-2):
            # Avoid duplicates
            if i > j and nums[i] == nums [i-1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total =  nums[j] + nums[i] + nums[left] + nums[right]
                if  total < target:
                    left += 1
                elif total == target:
                    quadruplets.append([nums[j], nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                else:
                    right -= 1

    return quadruplets

if __name__ == "__main__":
    sample_1 = ([4,1,2,-1,1,-3], 1)
    sample_2 = ([2, 0, -1, 1, -2, 2], 2)
    print('Sample 1:', sorted(sample_1[0]), sample_1[1])
    print('Find quadruplets equal to target in sample_1:', find_quadruplets(*sample_1))
    print('sample_2:', sorted(sample_2[0]), sample_2[1])
    print('Find quadruplets equal to target in sample_1:', find_quadruplets(*sample_2))


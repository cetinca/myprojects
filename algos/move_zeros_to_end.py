from typing import List

nums = [0, 1, 0, 3, 12]


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    helper = nums[:]
    i, j = 0, 0

    while i < len(nums):
        if j < len(helper):
            if helper[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1; j += 1
        else:
            nums[i] = 0
            i += 1


moveZeroes(nums)
print(nums)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == target == nums[j]:
                return [i, j]
            if nums[i] != target:
                i += 1
            if nums[j] != target:
                j -= 1
        return [-1, -1]

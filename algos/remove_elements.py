from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexes = []
        for i, v in enumerate(nums):
            if v == val:
                indexes.append(i)
        for i in indexes:
            nums.remove(val)
        return len(nums)


nums = [3, 2, 2, 3]
val = 3

s = Solution()

print(s.removeElement(nums, val))
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        memory = {}

        for num in nums:
            if num not in memory:
                count = sum([1 for n in nums if n == num])
                memory.update({num: count})
                if count > majority:
                    return num


print(Solution().majorityElement([1, 2, 2, 1, 2, 1, 5, 1, 1]))

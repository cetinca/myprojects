"""Input: nums = [4,1,2,1,2]
Output: 4
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # memo = set()
        # for n in nums:
        #     if n not in memo:
        #         memo.add(n)
        #     else:
        #         memo.remove(n)
        #
        # return memo.pop()
        return sum(set(nums)) * 2 - sum(nums)

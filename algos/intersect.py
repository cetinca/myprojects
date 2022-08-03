from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = set(nums1 + nums2)
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []

        for num in nums:
            r = min(count1[num], count2[num])
            for _ in range(r):
                result.append(num)
        return result

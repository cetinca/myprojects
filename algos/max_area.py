from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_, i, j = 0, 0, len(height) - 1
        while i < j:
            max_ = max(max_, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_


lst = [1, 8, 6, 2, 5, 4, 8, 3, 7]

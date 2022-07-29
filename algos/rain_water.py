import time
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        i, j = 0, len(height) - 1
        a, x, y = 0, 0, 0

        while i <= j:
            if i == j:
                a += h[i]
                break
            elif h[i] <= h[j]:
                if x < h[i]:
                    a += h[i]
                    x = h[i]
                else:
                    a += x
                i += 1
            else:
                if y < h[j]:
                    a += h[j]
                    y = h[j]
                else:
                    a += y
                j -= 1

        return a - sum(h)

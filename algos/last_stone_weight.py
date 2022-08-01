from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def find_max(s):
            if len(s) == 1:
                return s[-1]
            max1 = max(s)
            s.remove(max1)
            max2 = max(s)
            s[s.index(max2)] = max1 - max2
            return find_max(s)

        return find_max(stones)

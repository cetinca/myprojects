"""-2 ** 31 <= x <= 2 ** 31 - 1
"""

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r"^([ ])*([+-]?[0-9]+)"
        nums = re.match(pattern, s)

        if not nums: return 0

        return min(max(-2 ** 31, int(nums.group())), 2 ** 31 - 1)



s = Solution()

print(s.myAtoi("999999999999999999999999 is a number"))
print(s.myAtoi("-99999999999999999999999 is a number"))

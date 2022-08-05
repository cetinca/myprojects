from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows

        if n == 1:
            return [[1]]

        pre = self.generate(n - 1)
        temp = [0] + pre[-1] + [0]
        cur = []
        for i in range(len(temp) - 1):
            cur.append(temp[i] + temp[i + 1])
        pre.append(cur)
        return pre


print(Solution().generate(5))

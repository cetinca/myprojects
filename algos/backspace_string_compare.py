"""Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove(x):
            x = list(x)
            stack = []
            memo = []
            for i in range(len(x) - 1, -1, -1):
                if x[i] == "#":
                    stack.append("#")
                    x[i] = None
                elif stack:
                    stack.pop()
                    x[i] = None
                else:
                    memo.append(x[i])
            memo = [m for m in memo if m]
            return memo

        return remove(s) == remove(t)

class Solution:
    def isHappy(self, n: int, c=None) -> bool:
        if not c: c = {n}
        if n == 1: return True

        total = 0
        for a in str(n):
            total += int(a) ** 2

        if total in c:
            return False
        else:
            c.add(total)

        return self.isHappy(total, c)


s = Solution()

print(s.isHappy(19))

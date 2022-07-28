class Solution:
    def longestPalindrome(self, s: str) -> int:
        nums = {}
        for l in s:
            c = sum([1 for e in s if l == e])
            nums.update({l: c})
        pal = 0
        mid = 0
        for n in nums.values():
            if n % 2 == 0:
                pal += n
            else:
                pal += n // 2 * 2
                mid = 1

        return pal + mid

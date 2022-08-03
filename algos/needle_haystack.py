"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0

        while i < len(haystack):
            t, j = i, 0
            while j < len(needle):
                if t >= len(haystack):
                    return -1
                elif haystack[t] != needle[j]:
                    break
                t, j = t + 1, j + 1
            else:
                return i
            i += 1
        return -1

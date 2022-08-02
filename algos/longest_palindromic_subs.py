class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pal(text):
            len_ = len(text)
            i, j = 0, len_ - 1
            while i <= j:
                if text[i] != text[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        pal = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                temp = s[i:j]
                if is_pal(temp) and len(temp) > len(pal):
                    pal = temp

        return pal

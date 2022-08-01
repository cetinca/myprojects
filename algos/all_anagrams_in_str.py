import string
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens = len(s)
        lenp = len(p)

        ang = []

        alpha = string.ascii_lowercase
        countp = {l: 0 for l in alpha}
        countw = {l: 0 for l in alpha}

        def count_str(d, s):
            for l in s:
                d[l] += 1

        count_str(countp, p)
        # creating a window while moving right increasing new letter, decreasing old letter
        for i in range(lens):
            if i - lenp < 0:
                countw[s[i]] += 1
            else:
                countw[s[i]] += 1
                countw[s[i - lenp]] -= 1

            if countp == countw:
                ang.append(i - lenp + 1)

        return ang

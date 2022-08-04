from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #         if len(strs) <= 1:
        #             return strs[-1]

        #         min_ = (strs[0], len(strs[0]))
        #         for i in range(1, len(strs)):
        #             w, l = strs[i], len(strs[i])
        #             min_ = (w, l) if l < min_[1] else min_

        #         word = min_[0]

        #         strs.remove(word)

        #         i, j = 0, 0
        #         while i < len(word):
        #             for s in strs:
        #                 if word[i] != s[i]:
        #                     return word[:j]
        #             i, j = i + 1, j + 1
        #         else:
        #             return word
        if len(strs) <= 1: return strs[-1]

        l = min([len(word) for word in strs])
        i = 0

        for i in range(l):
            letters = set()
            for word in strs:
                letters.add(word[i])
            if len(letters) > 1: break
        else:
            i = i + 1 if l else 0
        return strs[0][:i]

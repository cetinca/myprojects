from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memo = dict()
        for word in words:
            memo.update({word: memo.get(word, 0) + 1})
        memo_s = sorted(memo.items(), key=lambda x: (-x[1], x[0]))
        memo_s = [word[0] for word in memo_s[:k]]
        return memo_s

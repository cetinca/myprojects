from typing import List

lst = [3, 7, 9, 1, 5, 3, 6, 4]


def maxProfit(prices: List[int]) -> int:
    min_ = float("inf")
    max_ = 0
    len_ = len(prices)
    for l in lst:
        min_ = min(min_, l)
        max_ = max(max_, l - min_)
    return max_


print(maxProfit(lst))

from typing import List

lst = [3, 7, 9, 1, 5, 3, 6, 4]


def maxProfit(prices: List[int]) -> int:
    prev = prices[0]
    margin = 0
    for l in lst:
        if l > prev:
            margin += l - prev
            print(l-prev)
            prev = l
        else:
            prev = l if prev > l else prev
    return margin


print(maxProfit(lst))

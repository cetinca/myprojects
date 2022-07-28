from typing import List


def minimumCardPickup(cards: List[int]) -> int:
    minPick = float('inf')
    print(float('-inf'))
    seen = {}
    for i, n in enumerate(cards):
        if n in seen:
            if i - seen[n] + 1 < minPick:
                minPick = i - seen[n] + 1
        seen[n] = i
    if minPick == float('inf'):
        return -1
    return minPick

minimumCardPickup([2, 4])
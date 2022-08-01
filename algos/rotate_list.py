from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    len_ = len(nums)
    t = [0]
    for i in range(len_):
        ni = (i + k) % len_
        t.append(nums[ni])
        nums[ni] = nums[i]
        nums[i] = t[0]
        print(t)
        print(nums)
        t = t[1:]

l = [1, 2, 3, 4, 5]
print(rotate(l,1))

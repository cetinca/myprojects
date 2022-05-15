import random

from datastructures_algorithms.generate_numbers import unsorted_ten


def check_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return
    return nums


print(unsorted_ten)

while True:
    random.shuffle(unsorted_ten)
    c = check_sorted(unsorted_ten)
    if c:
        break

print(unsorted_ten)

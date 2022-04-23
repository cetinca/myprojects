from generate_numbers import unsorted_numbers
from random import shuffle

numbers = unsorted_numbers[:10]
count = 0


def is_sorted(nums):
    global count
    count += 1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    print(count)
    return True


def sort(nums):
    while not is_sorted(nums):
        shuffle(nums)
    return nums


print(sort(numbers))

from generate_numbers import unsorted_numbers

numbers = unsorted_numbers[:10]

sorted_numbers = []


def min_index(nums):
    min_num = nums[0]
    index = 0
    for i in range(len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
            index = i
    return index


def sort(nums):
    while len(nums):
        min_ = nums.pop(min_index(nums))
        sorted_numbers.append(min_)
    return sorted_numbers


print(numbers)
print(sort(numbers))

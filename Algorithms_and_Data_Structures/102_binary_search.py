def binary_search(_list, target):
    first_index = 0
    last_index = len(_list) -1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        print(mid_index)
        if _list[mid_index] == target:
            return f"Index of target is {mid_index}"
        elif mid_index < target:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1


numbers = list(range(1,101))
result = binary_search(numbers, 12)
print(result)
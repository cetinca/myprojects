from generate_numbers import sorted_numbers


def binary_search(_list, target):
    if len(_list) == 0:
        return "Item not found!"

    mid_point = len(_list) // 2
    print(mid_point)
    if _list[mid_point] == target:
        return f"Item is {_list[mid_point]}"
    elif _list[mid_point] < target:
        return binary_search(_list[mid_point + 1:], target)
    else:
        return binary_search(_list[:mid_point], target)


print(sorted_numbers)
result = binary_search(sorted_numbers, 193)
print(result)

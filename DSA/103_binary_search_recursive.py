def binary_search(_list, target):
    if len(_list) == 0:
        return "Item not found!"

    mid_point = len(_list) // 2
    print(mid_point)
    if _list[mid_point] == target:
        return f"Item is {_list[mid_point]}"
    elif _list[mid_point] < target:
        return binary_search(_list[mid_point+1:], target)
    else:
        return binary_search(_list[:mid_point], target)


numbers = list(range(1,101))
result = binary_search(numbers, 100)
print(result)
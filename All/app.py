from datastructures_algorithms.generate_numbers import unsorted_hundred


def merge(left, right):
    lst = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
    while i < len(left):
        lst.append(left[i])
        i += 1
    while j < len(right):
        lst.append(right[j])
        j += 1

    return lst


def split_arr(arr):
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    return left, right


def merged_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = split_arr(arr)
    left = merged_sort(left)
    right = merged_sort(right)

    return merge(left, right)


print(unsorted_hundred)
print(merged_sort(unsorted_hundred))

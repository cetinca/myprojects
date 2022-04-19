from heapq import merge
from posixpath import split
import snoop

@snoop
def merged_sort(_list):
    if len(_list) <= 1:
        return _list

    left_half, right_half = split(_list)
    left = merged_sort(left_half)
    right = merged_sort(right_half)

    return merge(left, right)

def split(_list):
    mid = len(_list) // 2
    return (_list[:mid], _list[mid:])

def merge(left, right):
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):

    if len(list) <= 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

my_list = [99, 54, 78 , 1, 3, 89, -5, 75]

sorted = merged_sort(my_list)
print(sorted)
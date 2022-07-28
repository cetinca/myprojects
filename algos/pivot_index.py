arr = [1, 7, 3, 6, 5, 6]


def find_pivot(arr):
    total = sum(arr)
    len_ = len(arr)
    for i in range(len_):
        left = 0 if i == 0 else left + arr[i - 1]
        right = total - arr[i] - left
        if left == right:
            return i
    else:
        return -1


print(find_pivot(arr))

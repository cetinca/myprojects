w = ["asd", "axy", "b", "e", "a", "A", "AB", "Ab"]
n = [5, 4, 99, 102, 17, -5]


def invert(lst):
    if type(lst[0]) is str:
        return [word.swapcase() for word in lst]
    else:
        return lst


def sort_lst(lst):
    lst = invert(lst)
    for _ in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return invert(lst)


r = sort_lst(w)
print(r)
r = sort_lst(n)
print(r)

w = ["asd", "axy", "b", "e", "a", "A", "AB", "Ab"]
n = [5, 4, 99, 102, 17, -5]
m = [4, 4, "car"]


def invert(lst):
    for item in lst:
        if item.__class__() != lst[0].__class__():
            raise TypeError("List is multi-type, can not be sorted!")

    if type(lst[0]) is str:
        return [word.swapcase() for word in lst]
    else:
        return lst


def sort_lst(lst):
    try:
        lst = invert(lst)
        for _ in range(len(lst) - 1):
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
        return invert(lst)
    except TypeError as err:
        return err


r = sort_lst(w)
print(r)
r = sort_lst(n)
print(r)
r = sort_lst(m)
print(r)

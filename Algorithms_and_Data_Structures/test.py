numbers = [1, 789, 5, 75, 524, 132]

def min_index(lst):
    num, index = lst, 0
    for i in range(len(lst)):
        if lst[i] < num:
            num = lst[i]
            index = i
    return index


def insertion(lst):
    sorted_lst = []
    while len(lst):
        index = min_index(lst)
        number = lst.pop(index)
        sorted_lst.append(number)
    return sorted_lst


print(insertion(numbers))

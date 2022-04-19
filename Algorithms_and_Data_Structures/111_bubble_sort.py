numbers = [1, 789, 5, 75, 524, 132]

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

print(bubble_sort(numbers))

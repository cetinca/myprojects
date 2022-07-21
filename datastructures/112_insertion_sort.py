numbers = [1, 789, 5, 75, 524, 132]

def insertion_sort(my_list):
    list_length = len(my_list)
    for i in range(1, list_length):
        for j in range(i - 1, 0, -1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

    return my_list

print(insertion_sort(numbers))
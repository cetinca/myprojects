from string import ascii_letters

def linear_search(_list, target):
    for l in range(len(_list)):
        if target == _list[l]:
            return f"Index: {l}, Target: {_list[l]}"
    return "Target not found!"

my_list = ascii_letters
target = "X"
result = linear_search(my_list, target)
print(result)
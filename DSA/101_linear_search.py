from generate_numbers import numbers

def lin_search(target, lst):
    count = 0
    for i in range(len(lst)):
        count += 1
        if target == lst[i]:
            return f"Target: {target}, Index: {i}, Count: {count}"
    return "Not found!"


print(dict(enumerate(numbers)))
print()
print(lin_search(330, numbers))
from generate_numbers import sorted_numbers

def binary_search(target, lst):
    count = 0
    first_index = 0
    last_index = len(lst) - 1

    while first_index <= last_index:
        mid = (first_index + last_index) // 2 
        count += 1
        if target == lst[mid]:
            return f"Target: {target}, Index: {mid}, Count: {count}"
        elif target < lst[mid]:
            last_index = mid - 1
        else:
            first_index = mid + 1

    return f"Count: {count}, not found!"


print(dict(enumerate(sorted_numbers)))
for n in sorted_numbers:
    print(binary_search(n, sorted_numbers))

print(binary_search(938, sorted_numbers))
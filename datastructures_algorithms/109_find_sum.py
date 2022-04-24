from generate_numbers import sorted_numbers, unsorted_numbers
from time import perf_counter

def find_sum(target):
    count = 0
    for s in sorted_numbers:
        for u in unsorted_numbers:
            count += 1
            if s + u == target:
                return f"count: {count}, {target} =  {s} + {u}"
    return f"count: {count}, not found!"

_start = perf_counter()
print(find_sum(999))
print(f"time: {perf_counter() - _start}")

def find_sum(target):
    count = 0
    for s in sorted_numbers:
        count += 1
        num = target - s
        if num in unsorted_numbers:
           return f"count: {count}, {target} =  {s} + {num}"

    return f"count: {count}, not found!"

_start = perf_counter()
print(find_sum(999))
print(f"time: {perf_counter() - _start}")


def find_sum(target):
    count = 0
    uns = set(unsorted_numbers)
    for s in sorted_numbers:
        count += 1
        num = target - s
        if num in uns:
           return f"count: {count}, {target} =  {s} + {num}"

    return f"count: {count}, not found!"

_start = perf_counter()
print(find_sum(999))
print(f"time: {perf_counter() - _start}")

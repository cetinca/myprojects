def range_sum(numbers, start, end):
    total = 0
    for num in numbers:
        if start <= num <= end:
            total += num
    return total


input_numbers = [int(n) for n in input().split()]
a, b =  [int(n) for n in input().split()]
print(range_sum(input_numbers, a, b))

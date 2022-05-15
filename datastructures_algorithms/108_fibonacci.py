import re


def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def get_input():
    while True:
        user_input = input("Type an integer number below 29: ")
        pattern = r"^[12]?[0-9]$"
        if re.match(pattern, user_input):
            return int(user_input)


def fibo_gen(_num):
    num = _num
    j = 0
    while j <= num:
        yield fibonacci(j)
        j += 1


nums = fibo_gen(get_input())
while True:
    try:
        print(next(nums))
    except StopIteration as e:
        print(e)
        break

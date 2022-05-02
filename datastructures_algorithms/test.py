def fibonacci(num):
    if num == 0 or num == 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

def seq(target):
    x = 0
    while x <= target:
        yield fibonacci(x)
        x += 1

for i in seq(20):
    print(i)
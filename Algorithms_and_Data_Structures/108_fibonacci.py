def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

def fibo_lst():
    num = 0
    while True:
        yield fibo(num)
        num += 1

gen = fibo_lst()

for _ in range(20):
    print(next(gen))

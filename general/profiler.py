import cProfile

def fib_recursive(n):
    if n < 2:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)

cProfile.run("fib_recursive(30)")

print(fib_recursive(30))
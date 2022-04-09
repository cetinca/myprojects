import cProfile

def fib_list(n):
    if n < 2:
        return n

    sequence = [0, 1]

    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence[n]

cProfile.run("fib_list(30)")

print(fib_list(30))
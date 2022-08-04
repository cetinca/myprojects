def hammingDistance(x: int, y: int) -> int:
    a = bin(max(x, y))[2:]
    b = bin(min(x, y))[2:]
    d = len(a) - len(b)
    c = 0
    b = d * "0" + b
    print(a, b)
    for i in range(-1, -len(b)-1, -1):
        print(a[i], b[i])
        if a[i] != b[i]:
            c += 1
    return c


print(hammingDistance(1, 4))
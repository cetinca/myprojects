def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(climbStairs(5))
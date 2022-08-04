def reverse(x: int) -> int:
    num = 0
    digit = 0
    while x:
        digit = x % 10 if x > 0 else -(abs(x) % 10)
        x = (x - digit) // 10
        num = num * 10 + digit
    return num

print(reverse(34145))

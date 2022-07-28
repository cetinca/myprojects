nums = [128, 17]

steps = []

for num in nums:
    step = 0
    while num > 0:
        if num & 1 == 0:  # bitwise operation to check if the num is even.
            num >>= 1  # shifting right one step to divide 2.
        else:
            num -= 1
        step += 1
    steps.append(step)

print(steps)

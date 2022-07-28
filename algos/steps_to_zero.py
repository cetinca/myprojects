nums = [128, 17]

steps = []

for num in nums:
    step = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        step += 1
    steps.append(step)

print(steps)

def romans(lst):
    nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    pre = 0
    for i in range(len(lst)-1, -1, -1):
        if pre > nums[lst[i]]:
           sum -= nums[lst[i]]
        else:
            sum += nums[lst[i]]
        pre = nums[lst[i]]

    return sum


s = "MCMXCIV"

print(romans(s))

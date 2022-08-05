def hammingWeight(nums) -> int:
    s = [int(d) for d in bin(nums)[2:]]
    return sum(s)

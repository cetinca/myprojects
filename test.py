from collections import Counter

lst = "carrots carrots bread tomatoes onions apples tomatoes carrots tomatoes onions onions onions bread milk bread apples"
lst = lst.split()

count = {}
for l in lst:
    count[l] = count.get(l, 0) + 1

print(count)



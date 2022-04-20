import random
from generate_numbers import unsorted_numbers


def sort(lst):
  count = 0
  while True:
    count += 1
    random.shuffle(lst)
    for i in range(len(lst) - 1):
      if lst[i] > lst[i+1]:
        break
    else:
      print(count)
      return lst

print(sort(unsorted_numbers[:10]))

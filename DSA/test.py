import random
from generate_numbers import unsorted_numbers



def sort(lst):
  count = 0
  for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 - i): 
      count += 1
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
  print(f"count: {count}")
  return lst

print(sort(unsorted_numbers))
print("something")

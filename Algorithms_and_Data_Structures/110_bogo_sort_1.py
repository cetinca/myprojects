import random

numbers = [1, 789, 5, 75, 524, 132]

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  while not is_sorted(values):
    random.shuffle(values)
  return values

print(bogo_sort(numbers))
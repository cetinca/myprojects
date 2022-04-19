from random import shuffle

numbers = [1, 789, 5, 75, 524, 132]

def bogo(lst):
    while True:
        for i in range(len(numbers) - 1):
            if numbers[i+1] < numbers[i]:
                shuffle(numbers)
                break
        else:
            return numbers

bogo(numbers)
print(numbers)
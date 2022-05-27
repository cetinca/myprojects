import random

words = ["car", "apple", "blue"]

word = random.choice(words)

print("-" in word or "" in word)

# while "_" in word or "" in word:
#     word = random.choice(words)
#     print(word)
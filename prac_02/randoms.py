import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Line 1: 5 (smallest number that could've been generated: 5, largest 19)
# Line 2: 7 (smallest: 3, largest: 9)
# Line 3: 3.15 (2.5, 5.5)

print(random.randint(1, 101))

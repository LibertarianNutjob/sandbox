import random
a = random.sample(range(1, 100), 10)
even = [n for n in a if n % 2 == 0]
print even

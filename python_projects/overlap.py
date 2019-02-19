import random
set1 = random.sample(range(1, 20), 10)
set2 = random.sample(range(1, 20), 10)
print (set(set1) & set(set2))

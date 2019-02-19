import random
a = random.sample(range(1, 20), 10)
dest = []
for n in a:
    if n < 10:
        dest.append(n)
print dest

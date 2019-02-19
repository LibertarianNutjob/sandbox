import random

a = []
for x in range(0, 10):
    a.append(random.randint(1, 20))

b = []
for x in range(0, 10):
    b.append(random.randint(1, 20))

overlap_result = [i for i in a if i in b]
result = [i for i in overlap_result if overlap_result.count(i) == 1]

print a
print b
print result

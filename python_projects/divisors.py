x = int(input('Enter a number: '))
list = range(1, x+1)
divisors = []
for n in list:
    if x % n == 0:
        divisors.append(n)
print(divisors)

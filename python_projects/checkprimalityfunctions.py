num = int(raw_input('Enter a number: '))
list = [x for x in range(2, num) if num % x == 0]


def is_prime(n):
    if num > 1:
        if len(list) == 0:
            print 'prime'
        else:
            print 'NOT prime'
    else:
        print 'NOT prime'


is_prime(num)

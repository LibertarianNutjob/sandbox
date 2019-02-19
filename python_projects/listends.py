import random
a = random.sample(range(1, 20), 10)


def listends(userlist):
    return [userlist[0], userlist[len(userlist)-1]]


print a
print listends(a)

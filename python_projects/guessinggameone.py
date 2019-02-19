import random

num = random.randint(1, 9)
guess = 0
count = 0

while guess != num and guess != "exit":
    guess = raw_input("Please enter a number between 1 and 9: ")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess > num:
        print("You guessed too high")
    elif guess < num:
        print("You guessed too low")
    else:
        print("You guessed exactly right!")
        if count == 1:
            print("It only took you " + str(count) + " try")
        else:
            print("It only took you " + str(count) + " tries")

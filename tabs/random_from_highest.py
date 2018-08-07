import random

highest = 32
answer = random.randint(1, highest)

print("please guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("please guess higher")
    else:  # guess must be greater than number
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you've guessed it")
    else:
        print("sorry you've not guessed correctly")
else:
    print("you've got it first time")

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


# allows for infinite input
print("please guess a number between 1 and {}".format(highest))
guess = 0  # initialise to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("you've decided to quit")
        break
    if guess < answer:
        print("please guess higher")
    elif guess > answer:  # guess must be greater than number
        print("please guess lower")
    else:
        print("well done you've guessed it")

# to limit between 10 guesses no matter how high the number is use while loop

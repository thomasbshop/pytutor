name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print("{0} is {1} yrs old.".format(name, age))

if age >= 18:
    print("{0}, you have reached the legal age.".format(name))
    print("Register for your ID")
else:
    print("{0}, please come back in {1} years".format(name, (18-age)))


print("{0}, please guess a number between 1 and 10: ".format(name))
guess = int(input())

if guess < 5:
    print("please guess higher: ")
    guess = int(input())
    if guess == 5:
        print("Well done, you got it right")
    else:
        print("Sorry you have not guessed correctly.")
elif guess > 5:
    print("please guess lower")\
#Alert bad coding practice: duplication
    guess = int(input())
    if guess == 5:
        print("Well done, you got it right")
    else:
        print("Sorry you have not guessed correctly.")
else:
    print("You got it first time.")

#more efficient way
"""
if guess != 5:
    if guess <5:
        print("Please guess higher")
    else: #guess must be greater than 5
        print("please guess lower.")
        
    guess = int(input())
    if guess == 5:
        print("well done you've guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
"""
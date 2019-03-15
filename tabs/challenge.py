#Write a small program to ask for a name and age
#When both values have been entered, check if the person
#is the right age to go on an 18-30 holiday(they must be over
#18 and under 31 ).
#If they are, welcome them to the holiday. Otherwise print a
#polite message refusing them entry.

name = input("Hi there, what is your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if 17 < age < 31:
    print("welcome them to the holiday, {}".format(name))
else:
    print("you are not allowed")

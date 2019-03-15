age = int(input("How old are you:"))

#if (age >= 16) and (age <= 65):
#if 16 < age < 65:
if 15 < age < 66:
    print("Have a good day at work")

if (age >= 16) or (age <= 65):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

'''if (some_condition) or (some_function):
    # Do something'''
#python does not have a boolean datatype

x = input("Please enter some text:")
if x:
    print("you entered: ".format(x))
else:
    print("you did not enter anything")
    print(not true)
    print(not false)


#another way
if not (age < 18):
    print("You are old enough to vote")
    print("plese put an x in the box")
else:
    print("please come back in {0} years".format(18 - age))


#in is another keyword used in sequences
parrot = "Norwegian blue"
letter = input("enter a character: ")

if letter in parrot:
    print("please give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")
    
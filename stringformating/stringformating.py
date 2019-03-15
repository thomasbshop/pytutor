age = 23
print("My age is " + str(age) + " years.") #convert to string
#replacement fields.
print("My age is {0} years.".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}."
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
#multiline
print("""Jan: {0}
Feb: {1}
Mar: {0}
Apr: {2}
May: {0}
Jun: {2}
Jul: {0}
Aug: {0}
Sep: {2}
Oct: {0}
Nov: {2}
Dec: {0}
""".format(31, 28, 30))
#python2 alert
print("My age is %d years." % age)
print("My age is %d %s, %d %s." % (age, 'years', 5, 'months'))

#notice the number formatting with 4d and 2d
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %d." % (i, i**2, i**3))

print("\nPi is approximately %12.30f" % (22/7))

#python3
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}.".format(i, i**2, i**3))

print("\nPi is approximately {0:12.30f}".format(22/7))

"""when you dont want to use a replacement number more than 
 once, you can leave them and python will assume the order."""

for i in range(1, 20):
    print(i)
    print("I is now {0}".format(i))

number = "325,552,362,566,726,266"
for i in range(1, len(number)):
    print(number[i])


number = "325,552,362,566,726,266"
for i in range(1, len(number)):
    if number[i] in "0123456789":
        print(number[i])

number = "325,552,362,566,726,266"
for i in range(1, len(number)):
    if number[i] in "0123456789":
        print(number[i], end='')


#you can use this to edit numbers from a spreadsheet for example
number = "325,552,362,566,726,266"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("the number is {0}".format(newNumber))

#string characters
#lesser code same results
number = "325,552,362,566,726,266"
cleanedNumberChar = ''
for char in number:
    if char in "0123456789":
        cleanedNumberChar = cleanedNumberChar + char

newNumber = int(cleanedNumberChar)
print("the number is {0}".format(cleanedNumberChar))
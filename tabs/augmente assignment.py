# string characters
# lesser code same results
number = "325,552,362,566,726,266"
cleanedNumberChar = ''
for char in number:
    if char in "0123456789":
        # augmented assignment / more efficient
        cleanedNumberChar += char

newNumber = int(cleanedNumberChar)
print("the number is {0}".format(cleanedNumberChar))

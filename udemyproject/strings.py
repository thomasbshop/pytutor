greetings = "Hello"
name = input("Please enter your name: ")
print(greetings + ' ' + name)
bird = "African eagle"
#print the third character
print(bird[2])
#you can count backwards
print(bird[-4])
#print a slice
print(bird[3:7])
print(bird[3:])
print(bird[:7])
#print skipping in steps
print(bird[1:11:2])

number = "6,364,635,868,121,098,243"
print(number[1::4])
numbers = "0,1,2,3,4,5,6,7,8,9"
print(numbers[0::2])
string1 = "Thats"
string2 = " it!"
print(string1 + string2)
print("Dinning" "at" "the" "high" "table")
#you can multiply strings
print("hello" *8)
#check if a string is a substring of another/useful for searching
today = "Thursday"
print("day" in today)
print("thur" in today) #case sensitive
print("fri" in today)
# Create a program that takes some text and returns alist of all the characters in the text that are not vowels, sorted
# in alphabetical order. You can either enter text from the key board or initialise a string variable with a string.

someText = input("Please input some text: ")
vowels = {"a", "e", "i", "o", "u"}
# or vowels = frozenset("aeiou")
print(set(someText) - vowels)
print(sorted(set(someText) - vowels))

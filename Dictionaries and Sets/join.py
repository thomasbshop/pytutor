fish = ['barracuda', 'cod', 'devil ray', 'eel', 'tilapia', 'nile-perch', 'salmon', 'cat-fish']
letters = "abcdefghijklmnopqrstuvwxyz"
newString = ""
lettersString = ""

for c in fish:
    newString = ", ".join(fish)

print(newString)

for l in letters:
    lettersString = ", ".join(letters)

print(lettersString)

# example representing a map as a dictionary
# exit is a keyword
compass = {1: "north",
           2: "east",
           3: "south",
           4: "west"}

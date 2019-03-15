# Challenge extension

# we can extend the location names so that the user doesnt have to type only the direction, but also the location.

locations = {
    0: "You are sitting in-front of a computer learning python",
    1: "You are standing at the end of the road before a small brick building.",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in the valley beside a stream.",
    5: "You are in the forest"
}

# exits = [
#     {"Q": 0},
#     {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#     {"N": 5, "Q": 0},
#     {"W": 1, "Q": 0},
#     {"N": 1, "W": 2, "Q": 0},
#     {"W": 2, "S": 1, "Q": 0}
# ]
#
# if we are using a numerical key for a dictionary, the syntax for retrieving the dictionary value by key is the same
# as retrieving a list item by index
exits = {
    0: {"Q": 0},
    1: {"W": 2,  "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
}

namedExits = {
    1: {"2": 2, "3": 3, "5": 5, "4": 4},
    2: {"5": 5},
    3: {"1": 1},
    4: {"1": 1, "2": 2},
    5: {"2": 2, "1": 1}
}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "EAST": "E",
              "WEST": "W",
              "SOUTH": "S",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # instead of
    # availableExits = ", "
    # for directions in exits[loc].keys():
    #     availableExits += direction + ','
    # reason - don't concatinate strings
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are: " + availableExits + " ").upper()  # for uppercase input
    print()

    #  parse the user input using our vocabulary dictionary
    if len(direction) > 1:  # input is more than one letter
        words = direction.split()  # split the input for efficient proccessing
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]

    else:
        print("You cannot go to that direction.")


# We are using a numerical key for the dictionary, therefore the syntax for retrieving the dictionary value by key is
# the same as for retrieving a list item by index. So the code does not have to change

# we could have used list  over dictionaries in this challenge however dictionaries have the advantage in that
# insertion and deletion are extremely fast

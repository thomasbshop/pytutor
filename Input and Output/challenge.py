# modify this to use shelves instead of dictionaries. Do this by creating two programs.
# cave_initialise.py should create the two shelves (location and vocabulary) with the appropriate keys and values.
# cave_game.py will then use the two shelves instead of dictionaries. Apart from opening and closing the shelves,
# cave_game will need only two changes
# to the actual code - remember that shelve keys must be strings! Just to be clear, cave game.py will contain the code
# from line 45, everything before that (modified to use shelves) will be in cave_initialise.py



locations = {
    0: {"desc": "You are sitting in-front of a computer learning python",
        "exits": {},
        "namedExits": {}},
    1: {"desc": "You are standing at the end of the road before a small brick building.",
        "exits": {"W": 2,  "E": 3, "N": 5, "S": 4, "Q": 0},
        "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
    2: {"desc": "You are at the top of a hill",
        "exits": {"N": 5, "Q": 0},
        "namedExits": {"5": 5}},
    3: {"desc": "You are inside a building, a well house for a small stream",
        "exits": {"W": 1, "Q": 0},
        "namedExits": {"1": 1}},
    4: {"desc": "You are in the valley beside a stream.",
        "exits": {"N": 1, "W": 2, "Q": 0},
        "namedExits": {"1": 1, "2": 2}},
    5: {"desc": "You are in the forest",
        "exits": {"W": 2, "S": 1, "Q": 0},
        "namedExits": {"2": 2, "1": 1}}
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
    availableExits = ", ".join(locations[loc]["exits"].keys())
    # instead of
    # availableExits = ", "
    # for directions in exits[loc].keys():
    #     availableExits += direction + ','
    # reason - don't concatinate strings
    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are: " + availableExits + " ").upper()  # for uppercase input
    print()

    #  parse the user input using our vocabulary dictionary
    if len(direction) > 1:  # input is more than one letter
        words = direction.split()  # split the input for efficient processing
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]

    else:
        print("You cannot go to that direction.")
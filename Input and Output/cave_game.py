import shelve

locations = shelve.open("LocationsData")
vocabulary = shelve.open("VocabularyData")

loc = "1"
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    # instead of
    # availableExits = ", "
    # for directions in exits[loc].keys():
    #     availableExits += direction + ','
    # reason - don't concatenate strings
    print(locations[loc]["desc"])

    if loc == "0":
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


vocabulary.close()
locations.close()


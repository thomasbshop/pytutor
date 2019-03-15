import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    # for key in bike:
    #     print(key)

    print(bike["engine_size"])
    print(bike["colour"])

# shelve unlike dictionaries are file persistant therefore new files can be created because of a minimal error


# just like dictionaries we can use del to remove items from our shelve
del bike['engine_size']



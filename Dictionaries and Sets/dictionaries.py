# In previous sections we've seen how lists can be used to store lists of objects, and then we can actually retrieve
# those objects by their index.
# lists are generally used to store similar items. Although you can store numbers and strings in the same list if you
# think of a good reason for doing so.
# Now lists are also ordered sequences so as a result you can interact through all the items on the list and process
# them in order.
# Dictionaries and sets are both unordered collections. They both also guarantee that there will be no duplicates in
# that collection.
# Sets as similar to lists in that they're actually intended for storing similar items But you can't actually access
# individual items using an index. The set is unordered, so an index is meaningless in the context of a set.

# Dictionaries on the other hand Are again unordered and take key valued pairs. Now the values again are not accessed
# by an index but by means of a key. It's gonna give us a good opportunity to introduce two new string methods, split n
# join
# dictionaries can sometimes be reffered to as hashes.

fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour green citrus fruit"}

print(fruit)
print(fruit["lemon"])

# adding an entry to a dictionary
fruit["pear"] = "an odd shaped apple"

# modifying an entry
fruit["lime"] = "great with taquila"
# removing items
del fruit["lemon"]
fruit.clear()
print(fruit)

while True:
    dict_key = input("please enter a fruit: ")
    if dict_key == "quit":
        break
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("we don't have a " + dict_key)
    #
    # or we can do this instead
    description = fruit.get(dict_key, "we don't have a " + dict_key)
    print(description)

for snack in fruit:
    print(fruit[snack])


thisdict = {
    "apple": "green",
    "banana": "yellow",
    "cherry": "red",
    "avocado": "green",
    "mango": "yellow"
}

# sorted() method

# ordered_keys = sorted(list(thisdict.keys()))
# for f in ordered_keys:
#     print(f + "-" + fruit[f])

# or

for f in sorted(thisdict.keys()):
    print(f + "-" + thisdict[f])

for val in thisdict.values():  # not efficient
    print(val)

print('-' * 40)

for key in thisdict:  # more efficient
    print(thisdict[key])

#or

print(thisdict.keys())  # dict keys
print(thisdict.values())  # dict values


print(thisdict.items())

# creating dictionaries to tuples Dictionaries part 4 [2:40] - video tutorial
# dict() method
# there is a lot of interactions between lists dictionaries and tuples

# strings are immutable. dont concatenate strings in a loop. use the string join method


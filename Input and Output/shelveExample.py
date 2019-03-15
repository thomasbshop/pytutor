# shelving is used to serialise large sets of data efficiently unlike pickling
# loading a shelve can excecute code therefore dont use shelve files from untrusted sources
import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "A sweet, orange citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     # to confirm that the data has been processed correctly
#     print(fruit["lemon"])
#     print(fruit["grape"])


# once the shelve is open it can be used as a dictionary and we can access individual values using their keys as shown
# above in the print statements.
# There is no shelve literal. You cant initialise a shelve using a literal as we could with a dictionary.
# e.g. This is not advisable
#     '''
#     fruit = {'orange': "A sweet, orange citrus fruit",
#             'apple':"good for making cider",
#             'lemon':"a sour yellow citrus fruit",
#             'grape': "a small, sweet fruit growing in bunches",
#             'lime':"a sour, green citrus fruit" }
#
#     '''

# to leave your shelve open and close it manually change your syntax

fruit = shelve.open('ShelfTest')
# once this data ran on the first time it is automatically saved therefore no need to run again
fruit['orange'] = "A sweet, orange citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# # to confirm that the data has been processed correctly
# print(fruit["lemon"])
# print(fruit["grape"])
#
# # update info.
# fruit['lime'] = "great with tequilla"
# for snack in fruit:
#     print(snack + ":" + fruit[snack])

# Get data from a shelve
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     # Description with a default value
#     # description = fruit.get(shelf_key, "We don't have a " + shelf_key)
#
#     # a different way of doing it
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We dont have a " + dict_key)
#
# fruit.close()
#
# print(fruit)

# # A shelve is implemented using a database therefore the results may come out sorted
# for f in fruit:
#     print(f + " - " + fruit[f])
#

# # ordered alternative
ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " - " + fruit[f])


# A shelve key must be a string
# using methods for different output types
for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)
print(fruit.items())


fruit.close()

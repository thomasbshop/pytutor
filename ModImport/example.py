# print(dir())
# # print(dir(__builtins__))
# for m in dir(__builtins__):
#     print(m)

import shelve

print(dir())  # show python built-in items

print()
print(dir(shelve))  # show methods in shelve

# methods in shelve.Shelf object
for obj in dir(shelve.Shelf):
    print(obj)

print("=" * 40)

for obj in dir(shelve.Shelf):
    # sort out those starting with underscores
    if obj[0] != "_":
        print(obj)


# Some of the standard modules are actually written in c . They are responsible for system functionalities
# However many of them are written in python

help(shelve)

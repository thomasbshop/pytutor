# Now, a set in Python is unordered and doesn't contain duplicates, so  in that respect it's similar to a dictionary.
# However, unlike a dictionary, item's aren't accessed via a key. In fact, a set is probably more similar to a
# collection of dictionary keys. And the set members are hashed in the same ways dictionary keys are.
# Now, the elements in a set must be immutable objects. Again, just like dictionary keys.
# They also support the union and intersection operations that can be performed on sets.
# Now sets are generally used less often than the other data structures we've looked at so far, but that said, they
# can be very useful for cleaning up data.

# this is a syntax for creating dictionaries however we are only adding keys therefore sets
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("="*40)

wild_animals = set(["lion", "buffalo", "rhino", "zebra", "giraffe"])  # pass a list to the set function
print(wild_animals)

for animal in wild_animals:
    print(animal)

# adding a new member to a set
farm_animals.add("rooster")
wild_animals.add("horse")
print(farm_animals, wild_animals)

# sets are unordered therefore running multiple times will change the order

even = set(range(0, 40, 2))
print(even)
squres_tuple = (0, 4, 9, 16, 25)
print(squres_tuple)
print(set(squres_tuple))

print(len(even))

squares = set(squres_tuple)
print(len(squares))

# sets union

print(even.union(squares))
print(len(even.union(squares)))
print("="*40)

# intersection
print(even.intersection(squares))
print(even & squares)
print("="*40)

# set difference
print(sorted(even))
print(sorted(squares))
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))
print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

# look-up "difference_update", "symmetric difference
# symmetric difference can be thought of as the opposite of intersection
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print(sorted(even ^ squares))

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

# We can use discard and remove. The only difference between them is that removes would raise an error if the item to be
# removed doesn't exist and whereas discard won't actually raise an error in that scenario.
squares.discard(4)
squares.remove(16)
# squares.remove(8)  # will raise an error because 8 is absent in squares.
squares.discard(8)  # raises no error

try:
    squares.remove(8)
except KeyError:
    print("item 8 is not a member of the set.")

# issubset() and issuperset()
# frozen set - immutable cant be changed
even1 = frozenset(range(0, 56, 2))
# even1.add(3) will raise an error because even1 is immutable

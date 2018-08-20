fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour green citrus fruit"}

print(fruit)

veg = {"cabbage": "Is carrot really veg",
       "carrot": "I'll have carrot in place of this",
       "kales": "what are these",
       "french-beans": "Invasive species",
       "spinach": "can i have some more, please",
       "mushrooms": "Good food"}

print(veg)


# update method
# update method does not return anything
fruit.update(veg)
print(fruit)
print(veg.update(fruit))  # gives you none

# if you want to create a new dictionary use the copy method instead
nice_n_nasty = fruit.copy()
nice_n_nasty.update(veg)
print(nice_n_nasty)

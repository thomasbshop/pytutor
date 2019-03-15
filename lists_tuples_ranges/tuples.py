# tuples are similar to list but the difference is that they immutable - they cant be changed
# tuples - an ordered set of data
t = "a", "b", "c"  # or t = ("a", "b", "c")
print(t)

print("a", "b", "c")
print(("a", "b", "c"))  # add brackets when u want to print tuples

welcome = "Welcome to my nightmare", "Alice Copper", 1975
bad = "Bad Company", "Bad Company", 1974
Budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])

# you cannot make changes with tuples, e.g. item assignment, although tuples support indexing and slicing
imelda = imelda[0], "A change", imelda[2]
print(imelda)

# a type being immutable means u cant change the contents of an object once uve created it but it doesn't mean that your
# variable Can't be assigned a new object of that type, so that's an important clarification here.

# a dictionary key requires immutable objects e.g. tuple
# a list is intended to contain items of the same type - homogenous
# tuples are intended to store heterogenous stuff
# tuples help create robust code

title, artist, year = imelda
print(title)
print(artist)
print(year)

imelda1 = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
title1, artist1, year1, tracks = imelda1
print(title1)
print(artist1)
print(year1)
print(tracks)

# we are using an extra set of parenthesis to to create tuples within a tuple
print("title:{0}, artist: {1}, year: {2}, tracks{3}".format(title1, artist1, year1, tracks))

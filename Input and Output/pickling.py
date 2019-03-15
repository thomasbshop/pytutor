# pickle is a library that allows us to enclose complex Python objects as bytes.
# The pickle module is used to store and retrieve arbitrary Python objects (including entire collections)
# to and from disk
import pickle

# imelda1 = ("More Mayhem", "Emilda May", 2011, (
#     (1, "Pulling the rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")))
#
# # pickle.dump() - transform our object
# # pickle.load() - load our object back
#
# with open("imelda1_file.pickle", "wb") as pickle_file:
#     pickle.dump(imelda1, pickle_file)

# # title1, artist1, year1, tracks = imelda1
#
# # reading the data out of our imelda1_file.pickle
# with open("imelda1_file.pickle", "rb") as imelda1_pickled:
#     imelda2 = pickle.load(imelda1_pickled)
#
# print(imelda2)
# title1, artist1, year1, tracks = imelda2
# print(title1)
# print(artist1)
# print(year1)
# print(tracks)
# for track in tracks:
#     track_number, track_title = track
#     print(track)


# you can dump/load multiple objects
# the objects must be read in the same order that they are written
imelda1 = ("More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the rug"), (2, "psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda1_file.pickle", "wb") as pickle_file:
    pickle.dump(imelda1, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump("imelda1", pickle_file)

with open("imelda1_file.pickle", "rb") as pickled_file:
    imelda2 = pickle.load(pickled_file)
    even_list = pickle.load(pickled_file)
    odd_list = pickle.load(pickled_file)
    x = pickle.load(pickled_file)

print(imelda2)
title1, artist1, year1, tracks = imelda2
print(title1)
print(artist1)
print(year1)
print(tracks)
for track in tracks:
    track_number, track_title = track
    print(track_number, track_title)

print("*" * 40)

for i in even_list:
    print(i)

print("*" * 40)

for i in odd_list:
    print(i)

print("*" * 40)

print(x)

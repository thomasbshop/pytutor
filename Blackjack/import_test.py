import blackjack

# g = sorted(globals())
# for x in g:
#     print(x)

# print(__name__)
# blackjack.play()
# print(blackjack.cards)


# Underscore In Python
# use a single underscore after a name if it would otherwise conflict with a name built-in to python. (reserved)
# By convention stating a name with an underscore should indicate that it is treated as protected.
# Using import *, anything that starts with an underscore is not imported. it recorgnises the above convention
# Names that start and end with two underscores are the thing that u should'nt be changing.

# variables named '_' or '__' indicate a throw-away value. e.g. You may want to use tuples/or a section of the tuple.

personal_details = ("Thomas J", 723123456, "Nairobi", "6ft 0in")
name, phone_number, city, _ = personal_details  # you are not interested in the height, so u use "_".
print(phone_number)
print(_)

string = "0123456789"
# for char in string:
#     print(char)
my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for char in iter(string):
    print(char)

# create a list of items (you may use either strings or numbers in the list)
# then create an iterator using the the iter function.
# use a for loop to loop through n times, where n is the number of items in your
# list. Each time round the loop, use next() on your list to print the next item
# hint: use the len() function rather than counting the number of items in the list

items = ["monitor", "tissue box", "sandal",
         "spring", "wagon", "bookmark"]
list_of_items = list()
n = len(items)

for i in range(len(items)):
    next_item = next(iter(items))
    print("{0}: {1}".format(i+1, next_item))



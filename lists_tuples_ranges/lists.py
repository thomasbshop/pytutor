# list, range, tuple
ipAddress = input("Please enter an IP address: ")
print(ipAddress.count("."))
# a list is a list of things
vegetable_list = ["onions", "tomatoes", "cabbages", "kales", "parsley"]
vegetable_list.append("carrots")
for state in vegetable_list:
    print("The vegetable is " + state)

even = [2, 4, 6, 8, 10, 12]
odd = [1, 3, 5, 7, 9]
numbers = odd + even
array_numbers = [even, odd]

for number_set in array_numbers:
    print(number_set)
    for members in number_set:
        print(members)

# numbers.sort()
print(sorted(numbers))

# creating an empty list
list_1 = []
list_2 = list()
print("List 1: {0} and List 2: {1}".format(list_1, list_2))
if list_1 == list_2:
    print("New empty lists")

# python iterable
print(list("the lists are equal"))

# both variables refer to the exact same list
even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)

# create a new separate variable for another_even apart from even using the
# list() constructor
another_even = list(even)
another_even.sort(reverse=True)
another_reversed_even = sorted(even, reverse=True)

print(even)
# are they pointing to different variables
print(another_even is even)
# are they equal
print(another_even == even)

print(another_reversed_even)

# add to the program below so that if it finds meal without rice
# it prints out each of the ingredients of the meal
#

menu = list()
menu.append(["rice", "beans", "vegetables"])
menu.append(["ugali", "beef", "wild vegetables"])
menu.append(["ugali", "fish", "wild vegetables"])
menu.append(["roast chicken", "potatoes", "vegetables", "juice"])
menu.append(["rice", "mince meat", "vegetable"])
print(menu)

for meal in menu:
    if not "rice" in meal:
        for ingredient in meal:
            print(ingredient)


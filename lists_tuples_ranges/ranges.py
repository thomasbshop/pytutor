# ranges

print(range(100))

my_list = list(range(20))
odd = list(range(1, 20, 2))
even = list(range(0, 20, 2))
print(my_list, odd, even)

# range function consumes less memory but more computing power/time for processing

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index("f"))
print(my_string[9])

odd = range(1, 1000, 2)
print(odd)

print(odd[456])

sevens = range(7, 7000, 7)
print(sevens)

x = int(input("please enter a number < 1000000: "))
if x in sevens:
    print("The number {0} is divisible by seven".format(x))

decimals = range(0, 1000)
my_range = decimals[::3]
print(my_range)
print(list(my_range).index(45))

my_range_1 = decimals[3:40:3]
print(my_range_1 == range(3, 40, 3))
print(list(my_range_1).index(27))

# we get true for different set of values
# what is important is what range returns
# we are testing for equality of what the result is
print(list(range(0, 5, 2)), list(range(0, 6, 2)))
print(range(0, 5, 2) == range(0, 6, 2))

r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)

print('=' * 50)

for i in range(99, 0, -2):
    print(i)

print('=' * 50)

print(range(0, 100)[::-2] == range(99, 0, -2))

# we will not get any value for this because a -ve slice causes the value to be reversed
# take note of the start and end values
for i in range(0, 100, -2):
    print(i)

backstring = "!egaugnal lufrewop si a nohtyP"
print(backstring[::-1])

# another example
r = range(0, 10)
for i in r[::-1]:
    print(i)

# experiment with different ranges and slices to get a feel for how they work.
# remember that you can print the range as well as iterating through it to print
# its values , to check that your ranges are what you expected.
# you may also want to include things like.
o = range(0, 100, 4)
print(o)
# you notice that this iterates through the new list of steps 4 i.e. 0, 4, 8, 12 ...
p = o[::5]
print(p)
for i in p:
    print(i)

for state in ["using loops","the number is","pie chart graph", "fruit of the loom"]:
    print("This parrot is " + state)
    # print("This parrot is {0}".format(state))

for i in range(0, 100, 5):
    print("i is {0}".format(i))

# nesting loops
for i in range(0, 13):
    for j in range(0, 13):
        print("{0} time {1} is {2}".format(i, j, i*j), end='\t')
#   print("=================")
    print(' ')

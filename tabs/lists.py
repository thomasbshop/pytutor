# using continue and break
shopping_list = ["milk", "tea", "millet", "bread", "eggs", "wonder crust"]
for item in shopping_list:
    if item == "eggs":
        print("I am ignoring " + item)
        continue

    print("Buy " + item)
print(end='\n')

shopping_list = ["milk", "tea", "millet", "bread", "eggs", "wonder crust"]
for item in shopping_list:
    if item == "eggs":
        print("I am ignoring " + item)
        break

    print("Buy " + item)
print(end='\n')

# allow a loop to run all through the items

shopping_list = ["milk", "tea", "millet", "bread", "eggs", "wonder crust"]
no_eggs = ''
for item in shopping_list:
    if item == "eggs":
        no_eggs = item
        break
else:
        print("Now the list is fine")

if no_eggs:
        print("we don't want any eggs")

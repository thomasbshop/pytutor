# for i in range(10):
#    print("print the i's: {0}".format(i))

i = 0
while i < 10:
    print("print the i's: {0}".format(i))
    i += 1

available_exits = ["east", "west", "north", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("please choose a direction amongst {0}: ".format(available_exits))
    if chosen_exit == "quit":
        print("Game over")
        break

print("Aren't you glad you got there safely")



# using else with a while loop

available_exits = ["east", "west", "north", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("please choose a direction amongst {0}: ".format(available_exits))
    if chosen_exit == "quit":
        print("Game over")
        break

else:
    print("Aren't you glad you got there safely")

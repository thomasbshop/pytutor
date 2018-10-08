import datetime, random
import pytz
# Create a program that allows the users to choose one of up to 9 time zones from a menu.
# You can chose any zones you want from the all_timezones list. The program will then display
# the time in that timezone, as well as local time and UTC time. Entering 0 as the choice will
# quit the program.
# Display the dates and times in a format suitable for the user of your program to understand,
# and include the timezone name when displaying the chosen time.

timezones_list = {}
for i in range(1, 10):
    random_pick = random.choice(pytz.all_timezones)
    timezones_list[i] = random_pick
    print("\t{}: {}".format(i, timezones_list[i]))
print(timezones_list)

chosen_timezone_key = int(input("Please choose your timezone from the listed timezones above or '0' to exit: "))

while True:

    if chosen_timezone_key == 0:
        break
    else:
        chosen_timezone = pytz.timezone(timezones_list[chosen_timezone_key])
        print(type(chosen_timezone))
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        the_time = datetime.datetime.now(tz=chosen_timezone).strftime(fmt)
        print("The date and time for the timezone, {}, is {}.".format(chosen_timezone, the_time), end="\n")
        print("The local time is: {}".format(datetime.datetime.now().strftime(fmt)))
        print("UTC time is: {}".format(datetime.datetime.utcnow().strftime(fmt)))

        break

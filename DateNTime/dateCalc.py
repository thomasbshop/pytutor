# import time
#
# print(time.gmtime(0))  # returns tuple
#
# # print(time.localtime())  # returns tuple
#
# # print(time.time())
#
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)  # two ways of access
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)

import time
# from time import time as my_timer
# from time import process_time as my_timer
# python provides 3 more functions that we could use instead of the time() function to measure ellapsed time
# from time import perf_counter() as my_timer()  # use perf_counter or monotonic instead
# process_time() calculates the time the cpu uses rather than the real elapsed time. Useful in tasks like profiling code
# to use real time other than measured durations use the time() function
from time import monotonic as my_timer
import random


input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime((start_time))))
print("Stopped at " + time.strftime("%X", time.localtime((end_time))))

print("Your reaction time was {0} seconds ".format(end_time - start_time))

# reading peps for a certain python feature can be useful especially to know the reason why the feature is provided if
# you don't quite fully understand e.g.
# https://devguide.python.org/   https://www.python.org/dev/peps/pep-0418/

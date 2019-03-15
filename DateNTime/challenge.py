# write a small program to display information on the four clocks: i.e.
# time(), perf_counter(), monotonic(), process_time()

# use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks

import time

# timers = [time.time(), time.perf_counter(), time.monotonic(), time.process_time()]
timers = ["time", "perf_counter", "monotonic", "process_time"]

for i in range(len(timers)):
    print(i+1, timers[i] + ":", end="\n")
    print(time.get_clock_info(timers[i]), end="\n \n")


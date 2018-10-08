# # if you are dealing with both dates and time rather than just time, its better to use the "datetime" module rather than
# # just time even though time module also include dates
# # tzname(),
# # timezone()
#
# import time
#
# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current time zone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight saving time is in effect for this location")
#     print("\tthe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

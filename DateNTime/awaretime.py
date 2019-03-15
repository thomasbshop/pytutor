# ALWAYS WORK IN UTC
import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("local time: {}".format(local_time))
print("utc time: {}".format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("aware local time: {0}, \t timezone info: {1}".format(aware_local_time, aware_local_time.tzinfo))
print("aware utc time: {0}, \t timezone info: {1}".format(aware_utc_time, aware_utc_time.tzinfo), end="\n\n\n")


gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)  # custom epoch
print(gap_time)
print(gap_time.timestamp())

s = 1445733000
t = s + (3 * 60 * 60)

gb = pytz.timezone('GB')

dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
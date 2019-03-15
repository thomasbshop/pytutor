import datetime
import pytz

country = 'US/Eastern'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {0} is {1}".format(country, local_time))
print("UTC is {0}".format(datetime.datetime.utcnow()))

# for x in sorted(pytz.all_timezones_set):
#     print(x)
#
# for y in pytz.all_timezones:
#     print(y)


# list timezones per country
for z in sorted(pytz.country_names):
    print("{0}:{1}".format(z, pytz.country_names[z]), end=":")
    if z in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[z]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{0} - {1}".format(zone, local_time))
            print(zone)
    else:
        print("\t\t******NO TIMEZONE DEFINED******")


# remember to only work in UTC but convert the time when displaying to the user utcnow()


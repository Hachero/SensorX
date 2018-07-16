import pytz
import datetime


# for x in pytz.all_timezones:
#   print(x)

# print("\n------------------\t------------------\n")

# for x in sorted(pytz.country_names):
#   print(x + ":\t " + pytz.country_names[x])


# print("\n------------------\t------------------\t------------------\n")

for x in sorted(pytz.country_names):
  if x in pytz.country_timezones:
    print("{}:\t {}:\t {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))
  else:
    print("{}:\t {}:\t {}".format(x, pytz.country_names[x], "No TimeZone Defined"))

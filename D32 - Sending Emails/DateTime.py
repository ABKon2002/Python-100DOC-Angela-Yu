import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))
print('\n')

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(day)
print(month)
print(year)
# print(hour)
# print(minute)
# print(second)
print('\n')

# Creating a datetime object
my_birthday = dt.datetime(year = 2002, month = 2, day = 25)
print(my_birthday)
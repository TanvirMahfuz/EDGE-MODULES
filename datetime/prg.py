import datetime

print (datetime.datetime.now())
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print (datetime.datetime(2023, 5, 15))

from datetime import timedelta

# Creating a timedelta of 1 day, 2 hours, and 30 minutes
delta = datetime.timedelta(days=1, hours=2, minutes=30)
print(delta)  # Output: 1 day, 2:30:00

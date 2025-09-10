# Print Current Date and Time
import datetime
now = datetime.datetime.now()
print("current date and time:", now)
print("current year:", now.year)
print("current month:", now.month)
print("current day:", now.day)
print("current hour:", now.hour)    

# Convert String Into Datetime Object
date_string = "Feb 25 2020 4:20PM"
date_object = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print("date_object =", date_object)

# Subtract a Week From a Given Date
from datetime import datetime,timedelta
given_date = datetime(2020, 2, 25)
pastDate = given_date - timedelta(days=7)
print(pastDate)

#Format DateTime
given_date = datetime(2020, 2, 25)
full_date = given_date.strftime("%A %d %B %Y")
print(full_date)

#Find Day of Week
given_date = datetime(2020, 7, 26)
day_of_the_week = given_date.strftime("%A")
print(day_of_the_week)

# Add Week to Given Date
given_date = datetime(2020, 3, 22, 10, 0, 0)
print("Given Date:",given_date)
future_date = given_date + timedelta(days=7, hours=12)
print("Future Date:",future_date)

# Convert Datetime into String
given_date = datetime(2020, 2, 25)
stringDate = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(stringDate)

# Calculate the date 4 months from the current date
from datetime import datetime
from dateutil.relativedelta import relativedelta
given_date = datetime(2020, 2, 25).date()
future_date = given_date + relativedelta(months=+4)
print("Current Date:",given_date)
print("Four Months from now:",future_date)

# Calculate Days Between Two Dates

date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")
# Assign a variable that holds the number of days until your next birthday
import datetime

# assign the date of today
today_date = datetime.date.today()

# assign the date of my next birthday
next_birthday = datetime.date(2023, 5, 15)

# calculate the difference between the two dates
difference = next_birthday - today_date

# extract the days from the timedelta
difference_in_days = difference.days
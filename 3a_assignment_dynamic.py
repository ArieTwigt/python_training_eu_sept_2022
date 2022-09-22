# Assign a variable that holds the number of days until your next birthday
import datetime

# define the date of today
today_date = datetime.date.today()

# create variables for the different date parts
birthday_month = int(input("What is your birthday month?:\n"))
birthday_day = int(input("What is your birthday day?:\n"))
current_year = today_date.year

# compose the date for the next birthday
current_year_birthday = datetime.date(current_year, birthday_month, birthday_day)

# verify if my birthday is passed this year
birthday_passed = today_date > current_year_birthday

# conditional statement
if birthday_passed:
    next_year = current_year + 1
    next_birthday = datetime.date(next_year, birthday_month, birthday_day)
    difference = next_birthday - today_date
    difference_in_days = difference.days
    print(f"🎉 Your next birthday will be in {difference_in_days} days.")
else:
    next_birthday = datetime.date(current_year, birthday_month, birthday_day)
    difference = next_birthday - today_date
    difference_in_days = difference.days
    print(f"🎉 Your next birthday will be in {difference_in_days} days.")

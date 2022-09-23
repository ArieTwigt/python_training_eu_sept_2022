# Create a loop that prints the name of the day for the following 10 days
import datetime

today_date = datetime.date.today()

num_days = range(1,11)

for num in num_days:
    next_date = today_date + datetime.timedelta(days=num)
    next_day = next_date.strftime("%A")
    print(next_day)


pass
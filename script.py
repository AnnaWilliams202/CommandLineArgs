import sys
from datetime import datetime

args = sys.argv

if len(args) != 2:
    print("Usage: python script.py filename")

else:
    date = args[1]
    try:
        date = datetime.strptime(date, '%m-%d-%Y')
        day_of_week = date.strftime('%A')

        print(f'The day of the week for {date} is {day_of_week}')
    except ValueError:
        print("The date is not in the correct format. Please use MM-DD-YYYY format")
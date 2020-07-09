import sys
import calendar
from datetime import datetime

def calendars(month=datetime.now().month, year=datetime.now().year):

    try:
        print(calendar.month(int(year), int(month)))

    except:

        print("Your input must be in (4-digit-year, 1- or 2-digit-month) format. Please try again.")
        print(month)
        print(year)
        sys.exit()
    
if __name__ == "__main__":
# print(*sys.argv[1:])
calendars(*sys.argv[1:])

#option 2:

cy = datetime.now().year
cm = datetime.now().month
if len(sys.argv) == 2:
  cm = int(sys.argv[1])
elif len(sys.argv) == 3:
  cm = int(sys.argv[1])
  cy = int(sys.argv[2])
print(f"A calendar for year {cy}, month {cm}.")
print(calendar.monthcalendar(year=cy, month=cm))




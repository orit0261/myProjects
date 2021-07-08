import calendar
import datetime
now = datetime.datetime.now()
c_year = now.year
c_month = now.month
c_day  = now.day
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(c_year,c_month,4,1))
#check
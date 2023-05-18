import datetime
import time
import calendar

today_date=datetime.date.today()
today_date_time=datetime.datetime.now()
print("Today's date is: ",today_date)
print(type(today_date))
print("TOday date and time is: ",today_date_time)
print("")

today=datetime.date.today()
week_ago=datetime.timedelta(7)
gap=today-week_ago
print("The date week ago was: ",gap)
print("")

date_now=datetime.date.today()
format=date_now.strftime("%A %w %B %Y")
print(format)
print("")

given_date=datetime.date(2020, 7, 26)
print(given_date.strftime("%A"))
print("")

given_date=datetime.datetime(2020,7,26)
print("Adding nothing: ",given_date)
weeks=datetime.timedelta(weeks=1)
new_date=given_date+weeks
print("Adding 1 week: ",new_date)
hot=datetime.timedelta(hours=12)
new_date=new_date+hot
print("Adding 12 hours: ",new_date)
print("")

times=datetime.datetime.now()
current=times.strftime("%H:%M:%S")
print("Normal time: ",current)
time_msec=time.time()*1000
print("Time in millisec: ",time_msec)
print("")

date_time1=datetime.date(2020,2,25)
date_time2=datetime.date(2020,9,17)
date_diff=date_time2-date_time1
print("The difference is: ",date_diff)
print("")

now_date=datetime.date.today()
print(now_date)
print("")

given_date=datetime.date(2020, 2, 25)
to_string="%A %B %Y"
print("Date to sonverted to string:",given_date.strftime(to_string))
print("")

calen=calendar.calendar(2023)
print(calen)
year=2023
print(calendar.month(2023,4))
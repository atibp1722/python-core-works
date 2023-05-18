import time
import datetime

print(time.time())
print(time.ctime(1684236679.2346723))
print(time.localtime())
a=time.localtime()
b=time.mktime(a)
print(b)
c=time.asctime(a)
print(c)
d=time.strftime("%m/%d/%Y")
print(d)
e="18 August 2023"
s=time.strptime(e, "%d %B %Y")
print(s)
print("")

print(datetime.datetime(2023, 5, 4, 3, 17, 45, 24))
print(datetime.datetime.today())
print(datetime.datetime.now())
today=datetime.date(2022, 4, 17)
print(f"Date is {today}")
y=datetime.datetime.now()
times=datetime.time(17, 45, 45, 23283)
print(f"Time is {times}")
print(datetime.time.hour)
print(y.year)
date1=datetime.timedelta(days=27)
date2=datetime.timedelta(days=30)
date3=date1-date2
current_date=datetime.datetime.now()
new_year=datetime.datetime(2024,1,1)
time_rem=new_year-current_date
print(F"Next new year is in {time_rem}")
print(date3)
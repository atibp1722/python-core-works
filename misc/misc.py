import datetime, math, calendar, re

today=datetime.datetime.now()
print(today)
print(today.strftime("%d/%m/%Y %H:%M:%S"))

seconds=int(input("Enter seconds: "))
minutes=seconds/60
hours=minutes/60

print("Seconds:", round(seconds, 2))
print("Minutes:", round(minutes, 2))
print("Hours:", round(hours, 2))

diameter=int(input("Enter diameter for the circle: "))
radius=diameter/2

area=round(math.pi*(radius**2), 5)
print(f"Area of circle with diameter {diameter} is {area}")

base=int(input("Enter base for the triangle: "))
height=int(input("Enter height for the triangle: "))

tArea=round((base*height)/2, 5)
print(f"The area of triangle is {tArea}")

celcius=float(input("Enter temp in celcius: "))
cfarenheit=(celcius*9+5)/32
print(f"Temperature in farenheit {cfarenheit}")

farenheit=float(input("Enter temp in farenheit: "))
ccelcius=(farenheit-32)*(5/9)
print(f"Temperature in celcius {ccelcius}")
print("")

height=int(input("Enter yu height(cm): "))
weight=int(input("Enter your weight(kg): "))

height_to_meters=height/100
bmi=round((weight/height_to_meters**2), 2)
print(f"The BMI is {bmi}")

if bmi<18.5:
    print("You are underweight")
elif bmi>18.5 and bmi<25:
    print("You are normal weight")
elif bmi>25 and bmi<30:
    print("You are over weight")
else:
    print("You are obese")
print("")

year=int(input("Enter a year[YYYY]: "))
month=int(input("Enter month[1-12]: "))
print(calendar.month(year, month))
print("")

s_date=input("Enter start date: ")
e_date=input("Enter end date: ")

dates=s_date.split(" ")
s_year=int(dates[0])
s_month=int(dates[1])
s_day=int(dates[2])

s_date_ins=datetime.date(s_year, s_month, s_day)

datee=e_date.split(" ")
e_year=int(datee[0])
e_month=int(datee[1])
e_day=int(datee[2])

e_date_ins=datetime.date(e_year, e_month, e_day)

if e_date_ins<s_date_ins:
    print("Oops, something went wrong")
else:
    diff=(e_date_ins-s_date_ins).days

    if diff==0:
        print("The dates are the same")
    else:
        print(f"There are {diff} days between the two dates")
print("")

pattern='^My[\w\s]+[blue, black. white]$'
ans=input("Enter to check match: ")
if re.search(pattern, ans):
    print("It's a match")
else:
    print("No match")
print("")

n=int(input())
for i in range(n):
    card=input().replace(" ","")
    getAllDigits=[int(f)*2 if int(f)*2<10 else int(f)*2-9 for f in card[-2::-2]]
    sumEvenPlacedDigits=sum(getAllDigits)
    sumOddPlacedDigits=sum(map(int, card[::-2]))
    finalCalc=sumEvenPlacedDigits+sumOddPlacedDigits
    answer="yes"
    if finalCalc%10:
        answer="no"
    print(answer)
import math
import random

# if number is positive negative or zero
num=int(input("Enter a number: "))
if num<0:
    print("Negative")
elif num==0:
    print("Zero")
elif num>0:
    print("Positive")
else:
    print("Invalid input")
print(" ")

# max of three numbers
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter 3rd number "))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
print(" ")

# min of three numbers
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter 3rd number "))

if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)
print(" ")

# show season
season_num=int(input("Enter season number "))
if season_num<1 and season_num>5:
    print("Invalid season")
else:
    if season_num==1:
        print("Spring")
    elif season_num==2:
        print("Summer")
    elif season_num==3:
        print("Fall")
    elif season_num==4:
        print("Winter")
print(" ")

#check if number equal or not
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter 3rd number "))

if a==b and b==c and a==c:
    print("Equal")
else:
    print("Not equal")
print(" ") 

#number of days in a month
month=input("Enter name of month: ")
if month=="january":
    print(month.capitalize()," has 31 days")
elif month=="februrary":
    print(month.capitalize(), "has 28 days")
elif month=="march":
    print(month.capitalize(), "has 31 days")
elif month=="april":
    print(month.capitalize(), "has 30 days")
elif month=="may":
    print(month.capitalize(), "has 31 days")
elif month=="june":
    print(month.capitalize(), "has 30 days")
elif month=="july":
    print(month.capitalize(), "has 31 days")
elif month=="august":
    print(month.capitalize(), "has 31 days")
elif month=="spetember":
    print(month.capitalize(), "has 30 days")
elif month=="october":
    print(month.capitalize(), "has 31 days")
elif month=="november":
    print(month.capitalize(), "has 30 days")
elif month=="december":
    print(month.capitalize(), "has 31 days")
else:
    print("Invalid month entered")
print("")

# numbers in increasing or decereasing order
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter 3rd number "))

if a>b>c:
    print("Decreasing order")
elif a<b<c:
    print("Increasing order")
else:
    print("None")
print("")

# check vowels and consonants
text=input("Enter a text: ")
vowels=['a', 'e', 'i', 'o', 'u']
for data in text:
    if data.isalpha():
        if data in vowels:
            print(data, " is vowel")
        elif data not in vowels:
            print(data, " is consonant")
        else:
            print("Invalid")
    elif data.isnumeric():
            print(data, " is not an alphabet")
    elif data.isalnum:
        print(data, " is not an alphabet")
    else:
        print("Something went wrong")
print(" ") 

# quadriatic equation
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
c=int(input("Enter 3rd number "))

discriminant=(b**2)-(4*a*c)
if discriminant<0:
    print("Complex roots")
elif discriminant==0:
    result=-b/(2*a)
    print(result)
else:
    result_one=(-b - math.sqrt(discriminant))/(2*a)
    result_two=(-b + math.sqrt(discriminant))/(2*a)
    print(result_one,",",result_two)

# check if year is leap year or not
year=int(input("Enter the year "))
if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year, "is leap year")
        else:
            print("not leap year")
    else:
        print(year, "is leap year")
else:
    print(year," is not leap year")

#interactive calculator
print("-----This is a calculator-----")
num1=int(input("Enter a number "))
num2=int(input("Enter a number "))
choice=input("Enter your choice ")
match choice:
    case '+':
        sum=num1+num2
        print("The result of",num1,"+",num2,"is",sum)
    case '-':
        diff=num1-num2
        print("The result of",num1,"-",num2,"is",diff)
    case '%':
        div=num1/num2
        print("The result of",num1,"%",num2,"=",div)
    case '*':
        prod=num1*num2
        print("The result of",num1,"x",num2,"is",prod)
    case '%':
        rem=num1%num2
        print("The result of",num1,"%",num2,"is",rem)
    case '/':
        abs_div=num1//num2
        print("The result of",num1,"-",num2,"=",abs_div)
    case _ :
        print("No match found for operation")
print("")

# rock, paper, scissor game
player=input("Make your decision ")
option=["rock","paper","scissor"]
cpu=random.choice(option)
if player not in option:
    print("Option not avaialbe")
elif player==cpu:
        print("Tie game, cpu also has", cpu)
elif (player=="paper" and cpu=="rock") or (player=="rock" and cpu=="scissor") or (player=="scissor" and cpu=="paper"):
        print("You win, cpu has",cpu)
else:
    print("You loose, cpu has", cpu)  
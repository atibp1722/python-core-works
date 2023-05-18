import sys

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
try:
    div=num1/num2
    print(div)
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("This block is always exccuted")
print("-----------------------------")

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
try:
    div=num1/num2
    print(div)
except ZeroDivisionError as err:
    print(err)
print("Remaining code")
print("-----------------------------")

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
try:
    div=num1/num2
    print(di)
except Exception as val:
    print("Excepton without specifying name",val)
    print("Exception class",val.__class__)
print("Remaining code block")
print("-----------------------------")

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
try:
    div=num1/num2
    print(div)
except:
    print("Exception class using sys module",sys.exc_info()[0])
    print("Exception name using sys module",sys.exc_info()[1])
print("-----------------------------")

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
try:
    div=num1/num2
    print(div)
except (ZeroDivisionError, NameError, ValueError) as err:
    print(err)
else:
    print("Executed without exception")
print("------------------------------")

try:
    age=int(input("Enter your age: "))
    if age<1:
        raise ValueError
    print("Age cannot be less than 1 or negative value")
except ValueError:
    print("Please enter a valid age")
print("------------------------------")

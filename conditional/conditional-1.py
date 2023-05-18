# Q1
# var_1 and var_2 are operands 
# > is the operator

# Q2
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if (num1!=num2):
    print("The numbers are not same")
else:
    print("The numbers are the same")
print("-------------------")

# Q3
income=float(input("Enter income: "))
age=int(input("Enter age: "))
if (age>=18 and income>=15000):
    print("Approved for loan")
else:
    print("Not eligible for loan")
print("-------------------")

# Q4
age=int(input("How old are you: "))
ans=input("Have you passed qualifying exams?[Y/N] ")
if (age>=21 and ans=="Y"):
    print("You can enroll on course")
else:
    print("You cannot enroll on course")
print("-------------------")

# Q5
# w, a, b are operands = and + are operators
# x, c and d are operands = and ** are operators
# y, e and f are operands = and // are operators
# z, g and h are operands = and % are operators

# Q6
n=int(input("Enter first num "))
n1=int(input("Enter power to raise "))
print(n**n1)
print("-------------------")

# Q7
a=int(input("Enter number "))
b=int(input("Enter number "))
print(a//b)
print("-------------------")

# Q8
number=int(input("Enter a number "))
if (number%2==0):
    print("Number is even")
print("-------------------")

# Q9
num=int(input("Enter a number "))
if (num%2!=0):
    print("Number is odd")
print("-------------------")

# Q10
income=int(input("Enter income: "))
age=int(input("Enter age: "))
if (age>=21 and income>=21000):
    print("We are able to offer you loan")
else:
    print("Unfortunately, we are not able to offer you a loan")
print("-------------------")

# Q11
age=int(input("Enter your age "))
if(age<18):
    print("Not eligible to vote")
else:
    print("Eligible to vote")
print("-------------------")

# Q12
number=int(input("Enter a number "))
if(number%2==0):
    print("Even number")
else:
    print("Odd number")
print("-------------------")

# Q13
num=int(input("Enter any number "))
if (num%7==0):
    print("Divisible by 7")
else:
    print("Not divisible by 7")
print("-------------------")

# Q14
num=int(input("Enter any number "))
if (num%5==0):
    print("Hello")
else:
    print("Bye")
print("-------------------")

# Q15
unit=int(input("Enter no of units: "))
if(unit<=100):
    print("No charge")
if (unit>101 and unit<200):
    price=unit*5
    print(price)
if (unit>200):
    new_price=unit*10
    print(new_price)
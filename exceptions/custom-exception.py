# Step 1: Create an exception class and inherit it from the Base Exception Class i.e. Exception
# eg
# class InvalidAgeError(Exception):
#   pass (Error message can also be put here)

# Step 2: Raise exception for particular conditions inside try block
# condition: age<0
# try:
#   if age<0:
#       raise InvalidAge("error message")

# Step 3: Handle the exception that was raised using the except block
# except Exception as obj (obj is the variable that stores the error message that was raised)
#   print(obj)

from time import sleep
import sys

class DivideByTwoError(Exception):
    pass

try:
    num1=int(input("Enter 1st num: "))
    num2=int(input("Enter 1st num: "))
    if num2 == 2:
        raise DivideByTwoError("Sorry cannot divide by 2")
    result=num1/num2
    print("The result is",result)
except (DivideByTwoError, ZeroDivisionError) as err:
    print(err)
print("----------------------------------------------")

class InvalidAgeError(Exception):
    def __init__(self):
        print("Invalid age entered")
    pass
try:
    age=int(input("Enter age: "))
    if age<0:
        raise InvalidAgeError
    print(age)
except (InvalidAgeError) as val:
    print(val, end="")
print("----------------------------------------------")

class BalanceException(Exception):
    def __init__(self):
        print("Insufficient balance to withdraw")
    pass

class PinAttemptError(Exception):
    def __init__(self):
        print("No more pin attempts left, account is temporarily blocked")
    pass

pin_attempt=1

def withdraw():
    global pin_attempt
    pin_num=2468
    balance=10000
    pin=int(input("Enter pin number: "))
    if pin == pin_num:
        try:
            withdraw_amt=int(input("Enter amount to withdraw: "))
            temp_bal=balance-withdraw_amt
            if temp_bal<1000:
                raise BalanceException
            balance=balance-withdraw_amt
            print("Reamining balance in account:",balance)
        except (BalanceException) as var:
            print(var)
    else:
        ans=input("Do you wish to continue with transaction?[y/n]: ")
        if ans.lower()=='y':
            pin_attempt+=1
            try:
                if pin_attempt==4:
                    raise PinAttemptError
            except (PinAttemptError) as error:
                print(error, end="")
                sleep(100)
            else:
                withdraw()
        else:
            print("Thank you for using the application.")
            return
withdraw()
print("----------------------------------------------")

def format_traceback(exc_type, exc_value, exc_traceback):
    print("Oops, something went wrong")
    print(exc_type)
    print(exc_value)
    print(exc_traceback)
sys.excepthook=format_traceback

def test():
    print(69+"69")
test(0)
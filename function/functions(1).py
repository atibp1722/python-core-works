def greet():
    print("Hello")
    print("World")
greet()

def greet(fname, lname):
    print(f"Hello {fname} {lname}, welcome to python")
greet("Ram","Karki")

def get_greet(name):
    return f"Hello {name}"
print(get_greet("Ram"))

def increment(n1, n2):
    return n1+n2
print(increment(3,1))

def multiply(*numbers):
    total=1
    for number in numbers:
        total*=number
    return total
print(multiply(1,2,3,4))

def users(**user):
    print(user)
users(roll=1,name="Ram",address="ktm")

def fizzbuzz(num):
    if (num%3 == 0) and (num%5 == 0):
        return 'fizzbuzz'
    if num%3==0:
        return 'fizz'
    if num%5 == 0:
        return 'buzz'
    else:
        return num
print(fizzbuzz(15))

print("--------------------------------------")

def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num * factorial(num-1)
print("The factorial is:",factorial(4))

def fibonacci(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
n=int(input("Enter positive number: "))
for val in range(n):
    print(fibonacci(val))

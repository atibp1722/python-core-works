# check if number is prime or not
num=int(input("Enter a positive number: "))
if num>=2:
    for val in range(2, num):
        if num%val==0:
            print(num ,"is not prime number")
            break
    else:
        print(num , "is prime number")
else:
    print("Invalid input")

# prime number between two user entered number
lower=int(input("Enter a lower limit: "))
upper=int(input("Enter a upper limit: "))
for val in range(lower, upper):
    if val==1:
        continue
    for i in range(2, val):
        if val%i==0:
            break
    else:
        print(val)

# taking input and adding it to a set 
num1=int(input("Enter 1st positive number: "))
num2=int(input("Enter 2nd positive number: "))

if num1 %2 ==0:
    print("you entered even number")
    even_set=set()
    even_set.add(num1)
if num2 %2 !=0:
    print("you entered odd number")
    odd_set=set()
    odd_set.add(num2)
print(odd_set)
print(even_set)
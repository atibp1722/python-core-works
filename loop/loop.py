# printing positive integers from given range
num=int(input("Enter lower bound "))
num1=int(input("Enter upper bound "))
for val in range(num, num1+1):
    print(val)

# printing integers in descending order
a=int(input("Enter a number "))
for val in range(a,0,-1):
    print(val)

#sum of natural numbers
a=int(input("Enter a number "))
add=0
for val in range(1, a+1):
    add+=val
print("The sum is ", add)

#print multiplication table upto given number
a=int(input("Enter number "))
for val in range(a+1):
    for i in range(1,11):
        result=val*i
        print(a,"X",i,"=",result)

# print letters in alphabet in uppercase
for val in range(65, 91):
    print(chr(val))

# print even numbers within given range
num=int(input("Enter lower bound "))
num1=int(input("Enter upper bound "))
for i in range(num, num1+1):
    if i%2==0:
        print(i)

# print factorial of given number
a=int(input("Enter number "))
factorial=1
for i in range(1, a+1):
    factorial=factorial*i
print("The factorial of",a,"is",factorial)

# check number is prime or not
a=int(input("Enter number "))
if a>=2:
    for val in range(2, a):
        if a%val==0:
            print("Number",a,"is not prime")
            break
    else:
        print("Number",a,"is prime")
else:
    print("invalid input")

# print a simple pattern
a=int(input("Enter a number "))
for val in range(1, a+1):
    print("*"*val)

# reverse digits of a number
a=int(input("Enter a number "))
reverse=0
while a!=0:
    remainder = a%10
    reverse=(reverse*10)+remainder
    a=a//10
print(reverse)

# check if number palindrome or not
num=int(input("Enter a number "))
store_num=num
temp=0
while num>0:
    remainder=num%10
    temp=(temp*10)+remainder
    num=num//10
if store_num==temp:
    print(store_num,"is Palindrome")
else:
    print(store_num, "is not Palindrome")

# check if number is Armstrong number or not
num=int(input("Enter a number "))
temp=num
sum=0
while num!=0:
    remainder=num%10
    sum=remainder**3
    num=num/10
if sum==num:
    print(temp, "is Armstrong number")
else:
    print(temp, "is not Armstrong number")

# print floyd's triangle
num=int(input("Enter a number "))
counter=0
for val in range(1, num+1):
    for data in range(0, val):
        print(counter, end=" ")
        counter+=1
    print()

# reverse a string
text=input("Enter a random string ")
print(text[::-1])

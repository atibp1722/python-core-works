nums=[1,2,3,4,5]

def find_sum(s):
    if len(s)==0:
        return 0
    else:
        return s[0] + find_sum(s[1:])

print(find_sum(nums))
print("")

def fibo_sequence(n):
    if n==0 or n==1:
        return n
    else:
        return fibo_sequence(n-1) + fibo_sequence(n-2)

print(fibo_sequence(6))
print("")

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print("")

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
    
print(sum_of_digits(123))
print("")

def power(x,y):
    if y==0:
        return 1
    elif y==1:
        return x
    else:
        return x * power(x, y-1)

print(power(2,4))
print("")

def find_hcf(x, y):
    if y==0:
        return x
    else:
        return find_hcf(y, x%y)

print(find_hcf(12,16))
print("")

def palindrome_check(string):
    string=string.lower()

    if len(string)<=1:
        return True
    elif string[0]!=string[-1]:
        return False
    else:
        return palindrome_check(string[1:-1])

print(palindrome_check("anne"))
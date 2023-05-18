def multiples(greet, name):
    if greet=='hello':
        return greet
    if name=='ram':
        return name
    print(greet, name)
 
multiples("Hello", "Ram")
print("")

def greet(greet):
    if greet=='m':
        print("Good Morning")
    elif greet=='a':
        print("Good Afternoon")
    elif greet=='n':
        print("Good Night")
    else:
        print("Invalid option")
greet("a")
print("")

def addNums():
    a=2
    b=3
    sum=a+b
    print(sum)
addNums()
print("")

nums=[1,2,3,4,5,6,7,8,9,10]
def sum_recursion(num):
    length=len(num)
    if length==0:
        return 0
    else:
        return num[0]+sum_recursion(num[1:])
print("The sum is",sum_recursion(nums))
print("")

def division(n1,n2):
    try:
        result=n1/n2
        return result
    except ZeroDivisionError as error:
        print("Cannot divide by zero",error)
new_diviion=division
print("The result is",new_diviion(10,5))
print("")

lists=[]
def evenNums(l, h):
    for val in range(l,h):
        if val%2==0:
            lists.append(val)
    print(lists)
evenNums(4,30)
print("")

lists=['1','0','3','2','5','4']
def sortList(num):
    for i in num:
        num.sort()
    converted=tuple(num)
    maximum=max(converted)
    return maximum
print((sortList(lists)))
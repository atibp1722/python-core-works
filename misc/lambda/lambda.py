from functools import reduce

# anonymous functions having no name and no def keyword
# it can take any number of arguments but can only have one expression

# Normal function
def add(a,b):
    return a+b

sum=add(2,3)
print(sum)

# Lambda function
add=lambda a,b: a+b
print(add(1,2))

# Directly call lambda fucntion
(lambda a,b: a*b)(5,5) 

multiply=lambda x,y,z: x*y*z
print(multiply(x=2, y=3, z=4))

add=lambda x,y=5,z=10: x+y+z
print(add(x=5))

# adding=lambda *args: sum(args)
# print(adding(1,2,3,4,5))

func=lambda x, fun: x + fun(x)
func(20, lambda x: x*x)

(lambda x: (x%2 and 'even' or 'odd'))(10)

sub_string=lambda string: string in "welcome to lambda expression"
print(sub_string('lambda'))

nums=[1,5,2,4,3]
findMax=list(filter(lambda nums: nums>2, nums))
print(findMax)

num=[2,5,8,1,14]
findDiv=list(filter(lambda x: x%2==0, num))
print(findDiv)

list1=[1,2,3,4]
double_list_elem=list(map(lambda x: x*2, list1))
print(double_list_elem)

list2=[2,3,4]
power_list_elem=list(map(lambda x: x**2, list2))
print(power_list_elem)

list3=[1,2,3,4,5]
adds= reduce(lambda x,y: x+y, list3)
print(adds)

list4=[1,2,3,4]
product= reduce(lambda x,y: x*y, list4)
print(product)

# Lambda function for user defined quadriatic equation
def quadriatic_equation(a,b,c):
    return lambda x: a*x**2 + b*x + c
result=quadriatic_equation(2,4,5)
print(result(2))
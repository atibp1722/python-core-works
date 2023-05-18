import math

number=int(input("Enter a number: "))
length=int(math.log10(number))+1
# print(length)

temp=number

while(length>1):
    sum=0
    while(temp>0):
        sum+=temp%10
        # print(sum)
        temp=temp//10
        # print(temp)
    temp=sum
    length=int(math.log10(sum))+1
    # print(sum)

if(temp==1):
    print(f"{number} is magic number")
else:
    print(f"{number} is not magic number")
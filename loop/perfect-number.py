number=int(input("Enter any number: "))

sum=0
i=1

while i<number:
    if number%i==0:
        # print(i)
        sum+=i
    i+=1
    
if(sum==number):
    print(f"{number} is perfect number")
else:
    print("Not perfect number") 
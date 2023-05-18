import math
from itertools import permutations

lists=[1,2,3,4,5]
new_lists=[]
multiply=2
print(lists)
for val in lists:
    new_lists.append(val*multiply)
print(new_lists)
print("")

gender=["male", "female", "others"]
for val in gender:
    print(val,end=" ")
print("")

lists=[1,2,3,4,5]
new=tuple(lists)
maximum=max(lists)
print("Max:",maximum)
minimum=min(lists)
print("Min:",minimum)
print("")

lists=[1,2,3,4,5]
index=0
length=len(lists)
for val in range(0,length):
    lists.sort(reverse=True)
print("Max:",lists[0])
for val in range(0,length):
    lists.sort(reverse=False)
print("Min:",lists[0])
print("")

lists=[]
if len(lists)==0:
    print("Empty list")
else:
    print(lists)
print("")

places=['ktm','brt','pkr','bkt','ptn']
for val in places:
    print("Index of",val,"is",places.index(val))
print("")

players=['messi','pele','ronaldo','maradona','neymar','mbappe']
player_to_remove='maradona'
print("Before remove:",players)
for val in players:
    if player_to_remove in players:
        players.remove(player_to_remove)
        break
    else:
        print("No such player found")
print("After remove:",players)
print("")

nums=[1,2,3,2,4,5,8,6,7,4,3,2,1,7]
print(nums)
no_dups=[]
for data in nums:
    if data not in no_dups:
        no_dups.append(data)
print(no_dups)
print("")

food=['momo','pizza','momo','sandwich','burger','pizza','fries','burger']
print("Original:",food)
food_no_duplicates=[]
for val in food:
    if val not in food_no_duplicates:
        food_no_duplicates.append(val)
print("Remove duplicates:",food_no_duplicates)
print("")

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
count=0
for val in numbers:
    if val>3:
        count+=1
print("There are",count,"elements greater than 3")
print("")

nums=[1,2,3,4,5,6,7,8,9,10]
prime=[1,3,5,7]
difference=[]
for val in nums:
    if val not in prime:
        difference.append(val)
print("The difference between two lists:",difference)
print("")

a=[2,4,6]
b=[1,3,5]
distance=math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
print("The distance is:",distance)
print("")

nums=[1,2,3,4,5,6,7,8,9,10]
even=[2,4,6,8,10]
common=[]
for val in nums:
    if val in even:
        common.append(val)
print("The common elements:",common)
print("")

nums=[10,5,2,3,9,6,7,8]
print(nums)
print("Largest element:",max(nums))
if len(nums)==0:
    print("Empty list")
elif len(nums)>1:
    new_nums=sorted(nums)
    print("Second largest element:",new_nums[-2])
else:
    print(None)
print("")

nums=[10,5,2,3,9,6,0,7,1,8]
print(nums)
print("Smallest element:",min(nums))
if len(nums)==0:
    print("Empty list")
elif len(nums)>1:
    new_nums=sorted(nums)
    print("Second smallest element:",new_nums[1])
else:
    print(None)
print("")

alphabets=['a','b','c','d','e','a','e','b','i','o','u','c']
dicts={}
for val in alphabets:
    if val not in dicts:
        dicts[val]=1
    else:
        dicts[val]+=1
print(dicts)
print("")

water_body=['ranipokhari',['rara','fewa'],'sali nadi',['bagmati','godawari'],['hanumante','manohara']]
print(water_body)
new_list=[]
for val in water_body:
    if isinstance(val, list):
        for data in val:
                new_list.append(data)
    else:
        new_list.append(val)
print(new_list)
print("")

langs='python'
perms=permutations(langs)
for val in perms:
    print(val)
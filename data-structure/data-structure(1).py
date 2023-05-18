food=['sandwich','burger','fries','pizza','momo']
print("Original list:",food)
food.pop()
print("After popping from list:",food)
food.append("sausage")
print("After adding to list:",food)
food.remove("sausage")
print("After removing from list:",food)
print("")

num=[1,2,3,4,5,6,7,8,9,10]
odd_list=list()
print("Original list:",num)
for val in num:
    if val%2 != 0:
        odd_list.append(val)
print("Odd numbers in new list:",odd_list)
nums=[1,2,3,4,5,6,7,8,9,10]
even_list=list()
print("Original list:",nums)
for i in nums:
    if i%2 == 0:
        even_list.append(i)
print("Even numbers in new list:",even_list)
print("")

players=['messi','ronaldo','neymar','mbappe','vinicius','hazard']
length=len(players)
chunk=length//3
try:
    first_chunk=players[:chunk]
    print(first_chunk)
    second_chunk=players[0+length//3:0 + (2+length//3)]
    print(second_chunk)
    third_chunk=players[2+length//3:2 + (2+length//3)]
    print(third_chunk)
    first_chunk.reverse()
    print("After reverse first chunk:",first_chunk)
    second_chunk.reverse()
    print("After reverse second chunk:",second_chunk)
    third_chunk.reverse()
    print("After reverse third chunk:",third_chunk)
    print("")
except (IndexError, NameError, ValueError) as error:
    print(error,"SOmething went wrong")

player=['messi','ronaldo','neymar','mbappe','vinicius','messi','mbappe','hazard','messi']
count=0
for val in player:
    if val=='messi':
        count+=1
print("'messi' found in list",count,"times")
print("")

try:
    nums={1,2,3,4,5,6,7,8,9,10}
    primes={1,3,5,7}
    inter=nums.intersection(primes)
    print("The intersecting elements are",inter)
    for val in inter:
        if val in nums:
            nums.remove(val)
    print("After removing intersecting elements",nums)
except:
    print("An error occured")
print("")

langs={'c','c++','php','js','cobol','python','ruby','fortran'}
script_langs={'ruby','php','js'}
print("Before set clear",script_langs)
if langs.issuperset(script_langs):
    script_langs.clear()
    print("Cleared set",script_langs)
else:
    print("It is not superset")
print("")

listA=['duke','baylor','usc']
listB=['1','2','3']
listA.extend(listB)
setList=set(listA)
for i in setList:
        for j in listB:
            setList=set(list((list([i])+list([j]))))
            print(setList)
            break
print("")

player_info={
    'no':1,
    'position':'gk',
    'name':'oliver kahn',
    'country':'ger',
    'caps':100,
    'nation':'ger'
}
print(player_info.values())
player_info_value=list()
for val in player_info.values():
    player_info_value.append(val)
    if val=='ger':
        player_info_value.remove(val)
print(player_info_value)
print("")

momo=['chily','steam','fry','jhol']
for val in momo:
    if val=='fry':
        print("'fry' exists in list")
        break
else:
    print("Sorry cannot find")
momo_menu={
    'price':200,
    'type':'fry',
    'options':'yes',
    'sharing':'no'
}
for i in momo_menu.values():
    if i==val:
        print("'fry exists as value in dict'",momo_menu.values())
        print("List before delete",momo)
        momo.remove(val)
        print("List after delete",momo)
        break
print("")

lists=[1,2,1,3,1,2,3,4,5,3]
without_dups=[]
print("List with duplicates",lists)
for i in lists:
    if i not in without_dups:
        without_dups.append(i)
print("Without duplicates list:",without_dups)
new_tups=tuple(without_dups)
print("Converted to tuple",new_tups)
maximum=max(new_tups)
print("Max value element:",maximum)
minimum=min(new_tups)
print("Min value element:",minimum)
print("")
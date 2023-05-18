lenovo={
    'id':1,
    'model':'yoga',
    'price':99999,
    'year':2022,
    'ram':'16gb',
    'warranty':'yes'
}
for val in lenovo.keys():
    print(val, end=" ")
print("")
for val in lenovo.values():
    print(val, end=" ")
print("")
for val in lenovo.items():
    print(val, end=" ")
print("")
key_val="ram"
for val in lenovo.keys():
    if val==key_val:
        print(key_val,"exists in dictionary")
        break
else:
    print("No such key found")   
print("")

key="discount"
value=0.15
if key not in val:
    lenovo[key]=value
else:
    print(key,"Already exsists")
print(lenovo)
print("")

py_lang={
    'code':1,
    'course':'python',
    'level':'intermediate',
    'difficulty':'medium'
}
dj_lang={
    'code':2,
    'name':'django',
    'level':'advanced',
    'difficulty':'hard',
    'duration':2
}
new_dict=py_lang|dj_lang
print("Merged dictionary:",new_dict)
print("")

cost={
    'python':14999,
    'js':11999,
    'mern':16999,
    'graphics':9999,
    'flutter':17999
}
print(cost)
sorted_cost=sorted(cost.values())
print("All values:",sorted_cost)
for val in sorted_cost:
    print("Min value:",sorted_cost[0])
    print("Max value:",sorted_cost[-1])
    break
print("")

homedelivery={
    'cod':'yes',
    'esewa':'yes',
    'bank':'yes',
    'card':'yes'
}
new_dict=len(set(homedelivery.values()))
print(new_dict)
if (new_dict)==0:
    print("Nothing to show")
elif (new_dict)==1:
    print(True,"all values are same")
else:
    print(False,'not all values are same')
print("")

menu={
    'momo':150,
    'pizza':250,
    'burger':150,
    'fries':200,
    'sandwich':250,
    'roll':200,
    'chowmein':120,
    'sizzler':300
}
val_freq={}
for val in menu.values():
    if val not in val_freq:
        val_freq[val]=1
    else:
        val_freq[val]+=1
print(val_freq)
print("")

player=[['messi',10],['ronaldo',7],['mbappe','10'],['nemymar',11],['hazard',7]]
player_dict={}
for val in player:
    key=val[0]
    value=val[1]
    player_dict[key]=value
print(player_dict)
print("")

price={
    'fries':[100,120,150],
    'pizza':[200,250,300],
    'momo':[100,150,200],
    'burger':[150,175,200]
}
maxSum=0
for val in price.values():
    sums=sum(val)
    if maxSum==0:
        maxSum=sums
    elif maxSum<sums:
        maxSum=sums
print("The max sum of list elements:",maxSum)
print("")

word="groundlessness"
freq_dict={}
for val in word:
    if val not in freq_dict:
        freq_dict[val]=1
    else:
        freq_dict[val]+=1
print("Dict with letter count:",freq_dict)
print("")

players={
    'messi':[30,10,19],
    'ronaldo':[12,7,9],
    'hazard':[10,7,15],
    'neymar':[10,9,11]
}
print(players.values())
for val in players.values():
    list=sorted(val)
    print("Initial sort using sorted() method:",list)
for val in players.values():
    val.sort(reverse=True)
    print("Initial sort using sort() method:",val)
print("")


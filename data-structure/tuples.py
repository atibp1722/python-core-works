city=()
print(type(city))
city='ktm', 'ptn', 'bkt'
print(type(city))
players_list=['messi','ronaldo', 'neymar']
players_tuple=('messi','ronaldo', 'neymar')
players_list.append('mbappe')
print(players_list)
# players_tuple.append('mbappe')
# print(players_tuple)
even=(2,4,6,8)
print(even[-1])
print(city+even)
nested=(city, even)
print(nested)
lang=('python',)*5
print(lang)
print(even[1:3])
print("Reversed tuple:",city[::-1])
str='python'
print(tuple(str))
a,*b,c=city
print(a,b,c)
# del city
# print(city)
nums=(1,2,3,4,5,3,5,6,2)
print(nums.count(3))
print(sum(nums))
print(len(nums))
print(min(nums))
print(max(nums))
print(sorted(nums))
lst=[(1,2,3),(4,5,6)]
print(lst)
lst.append((7,8,9))
print(lst)
tup=(['a','b','c'],['d','e','f'])
print(tup)
print(tup[0])
tup[0].append('x')
tup[1].append('y')
print(tup)
tup[0].remove('b')
print(tup)
print("")
orgin=0,1,2,3,4,5,6,7,8,9
add=orgin+(10,)
new=add+orgin[::-1]
print(new)
# O(n) for list as it has to scan entire list
# O(1) constant time for iteration

sts={"ab",'a',1,2.5,"good",2,1}
new_set=set([1,'a',"abc",1,2,3])
print(sts)
print(new_set)
print("")
print(len(sts))
print(len(new_set))
for val in new_set:
    print("Elem in set:",val)
sts.add(4)
print(sts)
sts.update([1,2,4,"bad"])
print(sts)
sts.remove(2)
print(sts)
try:
    sts.remove(42)
except Exception:
    print("No such element to remove")
sts.discard(12)
print(sts)
sts.pop()
print(sts)
a={2,4,'a',6,'b'}
b={2,5,'e',6,'b'}
c=a.union(b)
print(c)
c=a.intersection(b)
print(c)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
g=frozenset(sts)
g.add(9)
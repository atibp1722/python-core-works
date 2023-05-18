food={"momo","pizza","burger","chwomein","sandwich"}
print("Set before: ", food)
food.clear()
print("After set cleared: ",food)
fried_food={"fries","momo","cutlet","patty"}
new_food=fried_food.copy()
print("New set with copied items: ",new_food)

players={"messi","ronaldo","mbappe","hazard"}
print("Set beofre adding: ",players)
players.add("neymar")
players.add("lewandowski")
players.add("kante")
print("Set after adding: ",players)
print("")

unis={"mit","oxford","stanford","caltech","harvard","nyu", "baylor","lsu"}
print("Set before popping: ",unis)
unis.pop()
unis.pop()
print("Set after popping: ",unis)
unis.remove("mit")
# unis.remove("iit") returns error as remove needs element to exist in list before it can remove it
print("Set after removing: ",unis)
unis.discard("nyu")
unis.discard("iit") #no error even though iit doesnot exist in the set
print("Set after discard: ",unis)
print("")

chicken={"hen","rooster","parent","layers","chick"}
meat={"mutton","buff","pork","fish"}
print("Before update: ",meat)
meat.update(chicken)
print("After update: ",meat)
vowel={'a','e','i','o','u'}
alphs={'a','b','c','d','e'}
print("Before update: ", vowel)
vowel.update(alphs)
print("After update: ",vowel)
langs={'c','php','js','python','java','cobol'}
print("before union: ",langs)
script_lang={'js','python','ruby','rust','r'}
print("before union: ",script_lang)
new_lang=langs.union(script_lang)
print("After union: ",new_lang)
odd={'1','3','5','7','9'}
even={'2','4','6','8','10'}
number=odd.union(even)
print("After union: ",number)
print("")

odd={'1','3','5','7','49','51','81'}
prime={'0','1','3','5'}
print("Before intersection ", odd)
print("Before intersection ", prime)
result=odd.intersection(prime)
print("After interection: ",result)
odd.intersection_update(prime)
print("After intersection update: ",odd)
a={'a','b','c','d','e'}
b={'a','e','i','o','u'}
print("Before intersection A: ",a)
print("Before intersection B: ",b)
show=a.intersection(b)
print("After A intersect with B:", show)
show1=b.intersection(a)
print("After B intersect with A:", show1)
print("")

odd={'1','3','5','7','49','51','81'}
prime={'0','1','3','5'}
print("Before difference ", odd)
print("Before difference ", prime)
test=odd.difference(prime)
print("After difference: ",test)
odd.difference_update(prime)
print("Difference update: ",odd)
a={'a','b','c','d','e'}
b={'a','e','i','o','u'}
print("Before difference A: ",a)
print("Before diffference B: ",b)
disp=a.difference(b)
print("After A difference with B: ",disp)
a.difference_update(b)
print("After difference update: ",a)
print("")

num={'2','4','8','16','32'}
num1={'2','4','5','6','7'}
print("Before symmetric difference ", num)
print("Before symmetric difference ", num1)
res=num.symmetric_difference(num1)
print("After symmetric difference: ",res)
num.symmetric_difference_update(num1)
print("After symmetric diff update: ",num)
a={'a','b','c','d','e'}
b={'a','e','i','o','u'}
print("Before symmetric difference A: ",a)
print("Before symmetric diffference B: ",b)
disp=a.symmetric_difference(b)
print("After symmetric diff: ",disp)
a.symmetric_difference_update(b)
print("After symmetric diff updte: ",a)
print("")

a={'a','b','c','d','e'}
b={'a','e','i','o','u'}
food={"momo","pizza","burger","chwomein","sandwich"}
fried_food={"fries","wings","cutlet","patty"}
print(a.isdisjoint(b))
print(food.isdisjoint(fried_food))
number={'1','2','3','4','5'}
even_number={'2','4'}
print(even_number.issubset(number))
print(number.issubset(even_number))
print(even_number.issuperset(number))
print(number.issuperset(even_number))
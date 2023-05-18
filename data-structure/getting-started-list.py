#STRING functions
str="hello world"
text=str.capitalize()
print(text)

str="Viel Glück und beste Wünsche"
text=str.casefold()
print(text)

str="hello world"
print(str.upper())
print(str.isupper())
str="HEllo WorlD"
print(str.lower())
print(str.islower())
print("")

str="python"
print(str.isalpha())
str="python123"
print(str.isalnum())
str="12345"
print(str.isnumeric())
print(str.isdigit())
print(str.isdecimal())
print("")

str="hello world"
text=str.endswith("ld")
print(text)
str="Hello world"
text=str.startswith("he")
print(text)
str="java with django"
print(str.index("j"))
print("")

str="Hello world"
print(str)
str_test="Hello world"
convert=list(str_test)
print(convert.count('o'))
text=str.count("l")
test=str.count(str)
print(text)
print(test)
strr=""
test1=len(str)
test2=len(strr)
print(test1)
print("")

str="python with django"
print(str.split())
str1=["h","e","1","1","0"]
river=['koshi','karnali','rapti','mechi']
test="-".join(river)
print(test)
text="".join(str1)
print(text)
print("")

#LIST functions
progs=['js', 'java', 'php', 'r']
langs=['c','c++','cobol','fortran']
print(progs)
copy_progs=list()
print("Before copy: ",copy_progs)
copy_progs=progs.copy()
print("After copy: ",copy_progs)
print("Before clear: ",copy_progs)
copy_progs.clear()
print("After clear: ",copy_progs)
""" langs=progs.copy()
print("After copying: ",langs) 
return error as list to be copied into needs to be empty to copy one list to another """
print("")

country=["nep","ind","chn","usa","uk"]
print("Before append: ",country)
country.append("jpn")
country.append("ger")
country.append("esp")
print("After append: ",country)

colleges=["ace","kusom","apex","ncc"]
print("Before combine: ",colleges)
schools=["ullens","gems","rosebud","paragon"]
print("Before combine: ",schools)
colleges.extend(schools)
print("After combine: ",colleges)
schools.extend(colleges)
print("After combine: ",schools)

food=['momo','pizza','sandwich','burger','chips']
print("Before inserting: ",food)
food.insert(2, 'patty')
food.insert(0, 'oats')
food.insert(4, 'chowmein')
print("After inserting: ",food)
print("")

dbs=['mssql','oracle','postgres','mysql','mongo']
""" sample=[]
print("Before popping: ",sample)
sample.pop()
print("After popping: ",sample)
cannot pop from an empty list """
print("Before popping: ",dbs)
dbs.pop()
print("After popping: ",dbs)

brand=['hp','acer','lenovo','dell','toshiba','ripple']
print("Before popping[index]: ",brand)
brand.pop(5)
brand.pop(0)
print("After popping[0] and [5]: ",brand)
""" brand.pop(4)
print("After popping [4]: ",brand)
cannot pop as index to pop exceeds size of the list items """

pizza=['cheese','chicken','veggie','mixed','mushroom']
print("Before removing['listElem']: ",pizza)
pizza.remove("veggie")
pizza.remove("mixed")
print("Before removing ['veggie'] and ['mixed']: ",pizza)
print("")

players=['messi','hazard','mbappe','neymar','isco','enzo','haaland']
print("Before reversing: ",players)
players.reverse()
print("After reversing: ",players)
print("Before sorting: ",players)
players.sort()
print("After sorting: ",players)
even=[8,2,4,10,0]
print("Before numbers sorted: ",even)
even.sort()
print("After numbers sorted: ",even)
even.sort(reverse=True)
print("Descending sort: ",even)
even.sort(reverse=False)
print("Ascending sort: ",even)
print("")

subjects=['bit','bba','csit','bca','bim','mbbs','bbs','bba']
print(len(subjects))
print(subjects.index("bba"))
print(subjects.count("bba"))
sub_conv=" ".join(subjects)
print(sub_conv)
print(len(sub_conv))
space_count=0
for val in sub_conv:
    if val==" ":
        space_count+=1
print("The number of spaces in string ",space_count)
subject_con="".join(subjects)
print(subject_con)
count_b=0
for i in subject_con:
    if i=='b':
        count_b+=1
print("Total number of b's are ",count_b)
str="hello"
print(str)
str1='hello'
print(str1)
str='I\'m blue dada dee'
print(str)
str='''multiple line
python string'''
print(str)
print("------String Methods------")
str="hello world"
print(f"The length of {str}:",len(str))
str='python'
print(str[2])
str='django'
for val in str:
    print(val, end="")
print("")

str12='beautiful'
for val in range(len(str12)):
    print(str12[val], end=" ")
print("")
str123='beautiful'
for val in range(-1, -len(str123)-1, -1):
    print(str123[val], end=" ")
print("")

stg='python'
print(stg[1:4])
print(stg[::4])
print(stg[4::])
print(stg[::-1])
print(stg.upper())
print(stg.lower())
print(stg.find('h'))
print(stg.index('o'))
print("")

stg='simplify'
print(stg.find('i'))
print(stg.index('i'))
print(stg.count('i'))
print("")

stg='welcome to the jungle'
data=stg.split(" ")
print(data)
str="simplify"
print(str.replace('sim','mis'))
str="this is python"
print(str.rpartition(" is "))
str1='hello'
str2='world'
print(str1+' '+str2)
name='Atib'
greet='Hello'
question="how are you"
print(f"{greet}, {name} {question}?")
print("")

str=input("Enter a sentence to reverse: ")
str=str+" "
temp=""
rev=""
for val in str:
    if val != " ":
        temp=val+temp
    else:
        rev=rev+" "+temp
        temp=""
print(rev)
print("")

str=input("Enter a string to check: ").lower()
temp=""
for val in range(-1, -len(str)-1, -1):
    temp=temp+str[val]
if str==temp:
    print("Palindrome")
else:
    print("Not palindrome")
print("")

inp=input("Enter a string: ")
st=inp.title()
en=inp.split()
mt=''
for val in en:
    mt=mt+val[:-1]+val[-1].upper()+' '
print(f"The modified string is {mt}")
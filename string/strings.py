import string

str=input("Enter a string: ")
print("Length of string:",len(str))
print("")

str=input("Enter a string: ")
index=int(input("Enter index: "))
if len(str)==0:
    print("empty string")
elif index<len(str):
    print("The element at index",index,"is:",str[index])
else:
    print("cannot do that")
print("")

str=input("Enter a string: ")
print("reversed string:",str[::-1])
print("")

str=input("Enter a string: ")
if len(str)==0:
    print("empty string")
else:
    print( "first and last 3 chars:",str[:3] + str[len(str)-3:] )
print("")

str=input("Enter a string: ")
new_str=""
length=len(str)
for val in range(length):
    if val%2==0:
        new_str+=str[val]
print("new string with all even index chars:",new_str)
print('')

str=input("Enter a string: ")
new_str=""
length=len(str)
for val in range(0,length,2):
    new_str+=str[val]
print("new string with only even index chars:",new_str)
print("")

str=input("Enter a string: ")
str_is_numeric=str.isnumeric()
if str_is_numeric is True:
    print("the string",str,"contains only numbers")
else:
    print("the string",str,"contains others too")
print("")

str=input("Enter a string: ")
remove=int(input("Enter position to remove: "))
length=len(str)
removed_str=""
if length==0:
    print("cannot remove from empty string")
for val in range(0,length):
    if val==remove:
        removed_str+=str[val]
        break
print("char removed at index",remove,"was",removed_str)

str="Good morning"
replace=input("Enter string to replace: ")
replace_char=str.replace("morning",replace)
print("replaced string",replace_char)

str="volcanic"
index=len(str)
replace=input("Char to replace: ")
for val in range(index):
    x=str.replace("c",replace)
print("string after replacing char:",x)
print("")

str="hello,good,afternoon"
comma=","
dot="."
new_str=str.replace(comma,dot)
print(new_str)
print("")

str=input("enter string separated by comma")
changed_str=""
comma=","
dot="."
for val in str:
    if val==comma:
        changed_str+=dot
    else:
        changed_str+=val
print("comma to dot:",changed_str)
print("")

str="The quick brown fox jumps over the lazy dog"
str.lower()
str=str.replace(" ","")
print(str)
new_set=set(str)
print(new_set)
if new_set==string.ascii_lowercase:
    print("the string is a pangram as it contains all letters of the alphabet")
else:
    print("sorry, the string is not a pangram")
print("")

str="Hello world, this is python string"
print("with spaces:",str)
str=str.replace(" ","")
print("spaces removed:",str)
print("")

str=input("Enter a string with spaces: ")
for val in str:
    if val==" ":
        str=str.replace(" ","")
print(str)
print("")

str=input("Enter a string: ")
prefix_value=input("Enter prefix value: ")
if str.startswith(prefix_value):
    print(str,"does start with prefix value",prefix_value)
else:
    print("sorry, no such prefix value found")
print("")

str=input("Enter a string: ")
suffix_value=input("Enter prefix value: ")
if str.endswith(suffix_value):
    print(str,"does end with suffix value",suffix_value)
else:
    print("sorry, no such suffix value found")
print("")

words=input("Enter a string: ")
print("before reverse:", words)
print("after reverse",words[::-1])
print("")

word=input("Enter a string: ")
new_word=[]
count=0
for val in word:
    if (word.count(val)>1) and (val not in new_word):
        new_word.append(val)
        count+=1
print("total repeats:",count)
if len(new_word)>0:
    for val in new_word:
        print("repeated chars:",val)
else:
    print(None)
print("")

word=input("Enter a string: ")
new_word=""
words=word.split(" ")
for val in words:
    new_word+="".join(sorted(val.lower()))+" "
print(new_word)

language="python"
print("Welcome to "+language)
print("Welcome to {}".format(language))
print(f"Welcome to {language}")
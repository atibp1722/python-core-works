import re

basicInfo='''
Ram is 24 years old
Rama is 25 years old'''

name=re.findall(r'[A-Z][a-z]*', basicInfo)
print(name)
age=re.findall(r'\d{1,3}', basicInfo)
print(age)

infoDict={}
x=0

for val in name:
    infoDict[val]=age[x]
    x+=1

print(infoDict)
print("")

testStr="This to inform that information is readily avaialbe in the internet"

srch=re.search("inform", testStr)
print(srch)

fnd=re.findall("inform", testStr)
for val in fnd:
    print(val)

itr=re.finditer("inform", testStr)
for val in itr:
    print(val)

testStr1="bat, hat, Rat, mat, pat, sat, cat"
srch=re.findall(r'[bhrmpa]at', testStr1)
for val in srch:
    print(val)
print("")

srch1=re.findall(r'[a-f]at', testStr1)
for val in srch1:
    print(val)
print("")

srch2=re.findall(r'[^a-j]at', testStr1)
for val in srch2:
    print(val)

testStr2="cat sat hat dat mat"
exp=re.compile(r"[d]at")
testStr2=exp.sub("pat", testStr2)
print(testStr2)
print("")

testStr3='''This is to
change a string
from lines
to spaces '''

rem=re.compile("\n")
testStr3=rem.sub(" ", testStr3)
print(testStr3)

landLine="6634567"
print("Digits:",len(re.findall('\d', landLine)))

pattern="1 12 123 1234 12345 123456"
print("Matches:",len(re.findall('\d{3,5}', pattern)))
print("")

landLines='''
6634567
01-4481445
4456 345
4456-789
016643874
+977-01-5512890'''

phones=re.search('\w{2}-\w{7}', landLines)
print(phones)
valid= re.findall('[+]''\w{3}-\w{2}-\w{7}',landLines)
print(f"Completely valid Nepal landline number {valid}")
print("")

patterns='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
email=input("Enter a email id: ")
if(re.search(patterns, email)):
    print(f"Email entered {email} is valid")
else:
    print("Email is not valid")
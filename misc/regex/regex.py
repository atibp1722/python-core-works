import re

testStr=''' Contrary to popular belief, Lorem Ipsum is not simply random text. 
It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. 
Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the 
more obscure Latin words, consectetur, cyclone and tyclone from a Lorem Ipsum passage, and going through the cites of the word in 
classical literature, discovered the undoubtable source. 
Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. 
This book is a treatise on the theory of ethics, very popular during the Renaissance. 
The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. '''

matches=re.search("Lorem", testStr)
print(matches)
print("--------------------------------------")

matches1=re.findall(r"[A-Z]+orem", testStr)
print(matches1)
print("--------------------------------------")

matches2=re.finditer(r"[a-z]+yclone", testStr)
for val in matches2:
    print(val) 
print("--------------------------------------")

matches3=re.finditer(r"\d{1}.\d{2}.\d{2}", testStr)
for i in matches3: 
    print(i)
print("--------------------------------------")

matches4=re.compile(r'um*')
pattern=matches4.finditer(testStr)
for val in pattern:
    print(val)
print("--------------------------------------")

matches5=re.compile(r'em|um')
pattern=matches5.finditer(testStr)
for val in pattern:
    print(val)
print("--------------------------------------")

matches6=re.compile(r'um\b')
pattern=matches6.finditer(testStr)
for val in pattern:
    print(val)
print("--------------------------------------")

matches7=re.compile(r'[A-Z][a-z]*'+r'rum')
pattern=matches7.finditer(testStr)
for val in pattern:
    print(val)
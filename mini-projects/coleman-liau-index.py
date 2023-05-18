text=input("Enter a string to test: ")

letters=0
for val in range(len(text)):
    if( (text[val]>="a" and text[val]<="z") or (text[val]>="A" and text[val]<="Z") ):
        letters=letters+1

words=1
for val in range(len(text)):
    if text[val]==" ":
        words=words+1

sentence=0
for val in range(len(text)):
    if (text[val]=="." or text[val]=="?" or text[val]=="!"):
        sentence=sentence+1

print("Total letters:",letters)
print("Total words:",words)
print("Total sentences:",sentence)

letter_ratio=letters/words
sentence_ratio=sentence/words

index=(0.0588*letter_ratio)-(0.296*sentence_ratio)-15.8
print(f"Coleman-Liau index is {index}")

if index<0:
    print("Before grade 1")
elif index>1 and index<15:
    print("Grade:",index)
else:
    print("After grade 10")
f=open("file-handling/modes/data.txt", mode='r+', encoding='utf-8')

data=f.read()
print(data)
f.write("\nr+ mode working")

f.close()

f=open("file-handling/modes/data1.txt", mode='w+', encoding='utf-8')

f.write("w+ mode working")
f.seek(0)
data=f.read()
print(data)

f.close()
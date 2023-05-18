import os

f = open("file-handling/hello.txt",mode='r')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.buffer)
print(f.closed)
print(f.readable())
print(f.writable())
f.close()
print("")

if os.path.isfile("file-handling/hello.txt"):
    f=open("file-handling/hello.txt",mode='r')
    data=f.read(12)
    print(data)
    f.close()
else:
    print("No such file exists")
print("")

f=open("file-handling/sentence.txt",mode='r')
data=f.readline(2)
data1=f.readline(4)
data2=f.readline(8)
print(data)
print(data1)
print(data2, end="")
f.close()
print("")

f=open("file-handling/sentence.txt",mode='r')
data=f.readlines()
for val in data:
    print(val)
f.close()
print("")

f=open("file-handling/hello.txt",mode='r')
print(f.tell())
f.read(3)
print(f.tell())
f.seek(0)
print(f.read())
f.close()
print("")

f=open("file-handling/hello.txt",mode='r')
letter_count=0
word_count=0
line_count=0
for line in f:
    line_count+=1
    line=line.strip("\n")
    letter_count+=len(line)
    word_list=line.split()
    word_count+=len(word_list)
f.close()
print(f"Total letters in file: {letter_count}")
print(f"Total words in file: {word_count}")
print(f"Total lines in file: {line_count}")
print("")

f=open("file-handling/data.txt",mode='w')
f.write("This content is written from python file.")
f.close()


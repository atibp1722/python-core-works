f=open("file-handling/first.txt", mode="r", encoding="utf-8")
s=open("file-handling/second.txt", mode="w", encoding="utf-8")
val=f.readlines()
for line in val:
    s.write(line)
f.close()
s.close()

wrtlns=open("file-handling/writelines.txt", mode="w", encoding="utf-8")
to_write=["hello\n", "world\n", "this is\n", "writelines methods"]
wrtlns.writelines(to_write)
wrtlns.close()

data='hello world, python x mode test'
f1=open("file-handling/xmode.txt", mode='x', encoding='utf-8')
f1.write(data)
f1.close()
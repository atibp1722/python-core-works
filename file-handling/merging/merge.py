files=[]
merged_data=" "
while True:
    fn=input("Enter name of the file:")
    files.append(fn)
    ans=input("Add another file? [y/n]: ").lower()
    if ans != 'y':
        break

for val in files:
    filename=val+'.txt'
    f=open(filename, mode='r', encoding='utf-8')
    merged_data=merged_data+f.read()+"\n"
    f.close()

print(merged_data)

with open("file-hanling/merging/final-merged.txt", mode="x", encoding='utf-8') as f:
    f.write(merged_data)
    print("Merging successful, thank you.")
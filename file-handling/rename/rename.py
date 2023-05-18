import os

path=input("Enter file path: ")
path.replace('\\', '/')
print(path)
print(os.listdir(path))

def main():
    i=1
    for fn in os.listdir(path):
        new_name=path+"txtfile"+str(i)+'.txt'
        i+=1
        old_name=path+fn
        os.rename(old_name, new_name)

main()
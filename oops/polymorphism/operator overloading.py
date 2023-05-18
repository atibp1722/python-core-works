# 1. check datatype of left operand
# 2. go inide that class
# 3. call __add__() function

a=2
b=2
print(a+b)
print(a.__add__(b))

a="hello"
b="world"
print(a+b)
print(str.__add__(a,b))
print("")

class Restuarent:
    def __init__(self, name, charge):
        self.name=name
        self.charge=charge

    def __gt__(self, other):
        return self.charge>other.charge

rest1=Restuarent('Nanglo', 800)
rest2=Restuarent('Alinas', 700)
print(rest1>rest2)
print("")

class Book:
    def __init__(self, title, price):
        self.title=title
        self.price=price
    
    def __add__(self, other):
        total=self.price+other.price
        return Book('Books', total)
    
    def __str__(self):
        return str(self.price)
    
book1=Book("Python for Dummies", 1200)
book2=Book("JS for Dummies",850)
book3=Book("R for Dummies",2500)

print("Price for books:",book1.price, book2.price)
print("Total price of books:",book1+book2+book3)
print("")

class Add:
    def add(self, n1, n2):
        print(n1+n2)
    
    def add(self, n1, n2, n3):
        print(n1+n2+n3)

# a=Add()
# a.add(5,6)
a=Add()
a.add(4,5,6)
print("")

class Add:
    def add(self, n1=None, n2=None, n3=None):
        if n1!=None and n1!=None and n3!=None:
            print("Three params addition:",n1+n2+n3)
        elif n1!=None and n2!=None:
            print("Two params add:",n1+n2)
        else:
            print("oops, something went wrong.")

ad=Add()
ad.add(1,2)
ad.add(1,2,3)
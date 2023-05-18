class Test:
    def __init__(self, name):
        self.name=name

    def __len__(self):
        i=0
        for val in self.name:
            i+=1
        return i

tst=Test("Employee")
print(f"Name is: {tst.name}")
print(f"Length is: {len(tst)}")
print("")

class Mobile:
    def __init__(self, brand, price, model):
        self.brand=brand
        self.price=price
        self.model=model
    
    def showDetails(self):
        return f"{self.model} {self.price}"
    
    def __repr__(self):
        return f"Mobile('{self.brand}', '{self.price}', '{self.model}')"
    
    def __str__(self):
        return f"{self.brand} -> __str__()"
    
    def __len__(self):
        return len(self.brand)
    
mob=Mobile("Samsung", 45000, "S-13")
print(repr(mob))
print(str(mob))
print(len(mob))
print(f"Brand name {mob.brand} & length is {len(mob)}")
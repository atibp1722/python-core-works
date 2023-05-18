class staff():
    ''' This class holds the basic information about staff '''
    # non-parameterized constrctor
    # def __init__(self): # self; it holds the memory address of the current object
    #     self.salary=15000
    #     self.age=24

    # parameterized constructor
    def __init__(self, name, address):
        self.name=name
        self.address=address
    
    # function inside the class; method
    def display(self):
        print(f"Name is {self.name} and address is {self.address}")
    # even if no constrcutor is specified, a default constructor is autmatically called
    # as a constructor is compulsorily needed to make and call python object

    # how oop works
    # 1. memory allocation for object
    # 2. memory reference returned to object
    # 3. memory reference automatilcally passed inside constructor
    # 4. constructor creates variable at particualr memmory reference

class instanceTest():
    pass

staff1=staff("Atib", "ktm")
# staff2=staff()
# print(staff2.age, staff2.salary)
print(staff1.name, staff1.address)
staff1.display()
print(staff1.__dict__)
print(staff1.name, staff1.address)
print(type(staff1))
print("------Built in class functions-------")
print(getattr(staff1, 'name'))
setattr(staff1, 'name', "Sita")
print(staff1.__dict__)
delattr(staff1, 'address')
try:
    print(getattr(staff1, 'address'))
except Exception as e:
    print(e)
print(hasattr(staff1, 'address'))
print("------Built in class attributes-------")
print(staff.__doc__)
print(staff.__dict__)
print(staff.__name__)
print(staff.__module__)
print(staff.__bases__)
print("------isinstance() method-------")
test=instanceTest()
print(isinstance(test, instanceTest))
print(isinstance(test, staff))

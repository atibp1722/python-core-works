class Person(object):
    salary=12000
    def __init__(self):
        print("Person constructor called")
        self.name=input("Enter your name: ")

class Staff(Person):
    salary=15000
    def __init__(self):
        print("Person constructor called")
        self.salary=int(input("Enter your salary: "))

class Manager(Staff):
    salary=20000
    def __init__(self):
        print("Person constructor called")
        self.department=input("Enter your department: ")
        print(f"Manager work at {self.department}")

mgr=Manager()
print(mgr.salary)
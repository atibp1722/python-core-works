class Employee:

    def setName(self, name):
        self.name=name
    
    def getName(self):
        print(f"The name is {self.name}")

emp=Employee()
emp1=Employee()

emp.setName(input("Please enter you name: "))
emp1.setName(input("Please enter you name: "))

print(emp.__dict__)
print(emp1.__dict__)

emp.getName()
emp1.getName()
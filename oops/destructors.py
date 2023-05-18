class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
    
    def __del__(self):
        print("Destructor called")

emp=Employee("Ram", 26)
emp.show()
del emp
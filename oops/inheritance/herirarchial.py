class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def show(self):
        print("Person constructor method")

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary

    def show(self):
        print("Teacher constructor method")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade=grade
    
    def show(self):
        print("Student constructor method")

class Staff(Person):
    def __init__(self, name,age, designation):
        super().__init__(name,age)
        self.designation=designation

    def show(self):
        print("Staff constructor method")

std=Student("Gita", 24, 90)
print(std.__dict__)
print(std.show())

tch=Teacher("Mahesh", 35, 27500)
print(tch.__dict__)
print(tch.show())

stf=Staff("Uttam", 46, "Principal")
print(stf.__dict__)
print(stf.show())
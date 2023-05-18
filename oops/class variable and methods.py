class Employee():
    
    department="IT" # class variable
    bonus=0.25
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod
    def get_bonus(cls):
        print(f"The bonus is {cls.bonus}")
        Employee.department="HR"

emp=Employee("Atib", 20000)
emp1=Employee("Ram", 22500)
print(Employee.department)
print(emp1.department)
Employee.department="Finance"
emp.department="QA"
print(emp.department)
print(emp.__dict__)
print(Employee.department)
Employee.get_bonus()
print(Employee.department)
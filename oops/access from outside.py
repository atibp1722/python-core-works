class Staff:
    def __init__(self, name, dept, salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print(f"Staff name: {self.name}")
        print(f"Staff dept: {self.dept}")
        print(f"Staff salary: {self.salary}")

class SalaryChange:
    @staticmethod
    def newSalary(obj):
        obj.salary=obj.salary+(stf.salary*0.15)
        obj.showDetails()

stf=Staff("Atib", "IT", 21000)
SalaryChange.newSalary(stf)
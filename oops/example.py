class Employee():
    sal_increment=1.25
    def __init__(self, fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    def increase(self):
        self.salary=self.salary*Employee.sal_increment

    @classmethod
    def sal_increase(cls, amount):
        cls.sal_increment=amount
    
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary=emp_string.split("-")
        return cls(fname, lname, salary)
    
    @staticmethod
    def holidayCheck(day):
        if day=='sunday' or day=='saturday':
            return False
        else:
            return True

class Staff(Employee):
    def __init__(self, fname, lname, salary, department, experience):
        super().__init__(fname, lname, salary)
        self.department=department
        self.experience=experience

    def increase(self):
        self.salary=self.salary*(self.sal_increment+0.25)

# emp=Employee("Ram", "KC", 23000)
# emp1=Employee("Rama", "Chhetri", 25000)
# emp2=Employee.from_str("Hari-Sharma-19000")
# emp.increase()
# emp1.increase()
# print(emp.salary)
# print(emp1.salary)
# Employee.sal_increase(2)
# emp.increase()
# emp1.increase()
# print(emp.salary)
# print(emp1.salary)
# print(emp2.fname, emp2.lname, emp2.salary)
# print(emp2.holidayCheck('friday'))
staff=Staff("Biswas","KC",22500,"HR",2)
print(staff.department, f"Old salary: {staff.salary}")
staff.increase()
print(f"Updated salary: {staff.salary}")
print("")
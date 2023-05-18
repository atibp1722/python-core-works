class Employee:
    def __init__(self):
        # prefix variable name by "__" to make it private
        # prefix variable name by "_" to make it protected
        self.__ssn='A2CDR-102FC' 
        self.__bank_account=108017501662
    
    def show(self):
        self.__ssn='TER2B-875ER' 
        print(f"Social security number {self.__ssn} and bank account number {self.__bank_account}")

emp=Employee()
emp.show()
print(emp.__dict__)
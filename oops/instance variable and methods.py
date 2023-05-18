class Student():
    
    # instance variable using constructor
    def __init__(self, id, name, address):
        self.id=id
        self.name=name
        self.address=address

    # instance method
    def show(self):
        print(f"Id {self.id}, name {self.name} and address {self.address}")
    
    def change_data(self):
        self.name="Abihav"
        self.address="Brt"

std=Student(1, "Abhas", "Ktm")
std1=Student(2, "Anwit", "Bkt")
std2=Student(3, "Asim", "Ptn")

# instance variable outside the class
std.age=24
print(std.__dict__)
std1.name="Rama"
print(std1.__dict__)
std2.show()
std1.change_data()
print(std1.__dict__)
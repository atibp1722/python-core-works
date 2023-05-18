class Outer:
    def __init__(self):
        print("Outer constructor")
    
    def display(self):
        print("This is display of outer")

    class Inner:
        def __init__(self):
            print("Inner constructir")

        def show(self):
            print("This is show of inner")

out=Outer()
inn=out.Inner()
inn.show()
print("")

class Student:
    def __init__(self, id, name, dd, mm, yy):
        self.id=id
        self.name=name
        self.dob=self.DOB(dd, mm ,yy)
    
    def showDob(self):
        print(f"The name is {self.name} and id is {self.id}")
        self.dob.showDob()

    class DOB:
        def __init__(self, dd, mm, yy):
            self.dd=dd
            self.mm=mm
            self.yy=yy
        
        def showDob(self):
            print(f"The Dob is {self.dd}-{self.mm}-{self.yy}")
        
stud=Student(1, "Atib", 12, 3, 1998)
stud.showDob()
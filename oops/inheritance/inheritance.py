class Employees:

    bonus=0.25

    def display(self):
        print("Employee method")

class Manager(Employees):

    tada=0.35

    def show(self):
        print("Manager method")

mgr=Manager()

mgr.show()
mgr.display()
print(mgr.bonus)
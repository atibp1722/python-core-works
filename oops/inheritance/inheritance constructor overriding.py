class Parent:
    def __init__(self):
        print("Parent constructir called")
        self.vehicle="Car"

class Child(Parent):
    def __init__(self):
        print("Child constructir called")
        self.vehicle="Scooter"

chd=Child()
print(chd.__dict__)
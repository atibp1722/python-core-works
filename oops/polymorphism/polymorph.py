players=['messi','maradone','pele']
player="boateng"

for val in reversed(players):
    print(val)

for val in reversed(player):
    print(val, end=" ")

class Vehicle:
    def __init__(self, name, wheels):
        self.name=name
        self.wheels=wheels
    
    def showDetails(self):
        print(f"Name of vehicle is {self.name}")
        print(f"Number of wheels in vehicle is {self.wheels}")

    def maxCapacity(self):
        print("Cannot exceed 2500 CC")
    
    def maxGears(self):
        print("Cannot exceed 6")

class Bike(Vehicle):
    def maxCapacity(self):
        print("Cannot exceed 1200 CC")
    
    def maxGears(self):
        print("Cannot exceed 4")

vehicle1=Vehicle("Car", 4)
bk=Bike("Yamaha", 2)
vehicle1.showDetails()
bk.showDetails()
vehicle1.maxCapacity()
bk.maxCapacity()
print("")

class Card:
    def __str__(self):
        return "This is custom card class object"
crd=Card()
print(crd)
print("")

class Cart:
    def __init__(self, cart1, cart2, cart3):
        self.fashion=cart1
        self.food=cart2
        self.electronics=cart3
    
    def __len__(self):
        print("Items in cart")
        return len(self.fashion)+len(self.food)+len(self.electronics)

shopping=Cart(['pant','shirt','sweater'],['momo','fanta'],['airpods'])
print(len(shopping))
print("")

class Honda:
    def fuel(self):
        print("It runs on petrol")

    def maxSpeed(self):
        print("Max spped is 180")

class Tata:
    def fuel(self):
        print("It runs on electricity")
    
    def maxSpeed(self):
        print("Max speed is 150")
        
def car_specs(obj):
    obj.fuel()
    obj.maxSpeed()

honda=Honda()
tata=Tata()

car_specs(honda)
car_specs(tata)
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def maxSpeed(self):
        pass

    def gears(self):
        print("4 gears min")

class Audi(Car):
    def maxSpeed(self):
        print("Audi max speed is 200km/h.")

class Jaguar(Car):
    def maxSpeed(self):
        print("Jaguar max speed is 170km/h.")

class Bmw(Car):
    def maxSpeed(self):
        print("Bmw max speed is 180 km/h.")

a=Audi()
j=Jaguar()
b=Bmw()
a.maxSpeed()
j.maxSpeed()
b.maxSpeed()
a.gears()
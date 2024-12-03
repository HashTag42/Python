#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Create a superclass
class Vehicle():
    # "Constructor" function
    def __init__(self, bodystyle):
        self.bodystle = bodystyle
    def drive(self, speed):
        self.mode  = "driving"
        self.speed = speed
    def __str__(self):
        return f"{self.bodystle}"

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.enginetype = enginetype
        self.wheels = 4
        self.doors = 4
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, self, "at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        self.enginetype = enginetype
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, self, "at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1  = Motorcycle("gas", True)

print(car1.enginetype)
print(car2.doors)
print(mc1.wheels)

car1.drive(30)
car2.drive(40)
mc1.drive(50)
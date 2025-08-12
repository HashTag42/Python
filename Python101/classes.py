from datetime import date
from enum import Enum


class Sex(Enum):
    FEMALE = "female"
    MALE = "male"


class Human():
    def __init__(self, sex: Sex, dob=date.today()):
        if not isinstance(sex, Sex):
            raise TypeError("'sex' must be a member of the Sex enum")
        self.sex = sex
        if not isinstance(dob, date):
            raise TypeError("'dob' must be a date")
        self.dob = dob

    def age(self) -> date:
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age


class Person(Human):
    def __init__(self, sex: Sex, dob: date, name: str):
        super().__init__(sex, dob)
        self.name = name

    def __str__(self) -> str:
        return f"{self.name} is a {self.age()} years old {self.sex.value}."


class Man(Person):
    def __init__(self, name: str, dob: date):
        super().__init__(Sex.MALE, name, dob)


class Woman(Person):
    def __init__(self, name: str, dob: date):
        super().__init__(Sex.FEMALE, name, dob)


class Vehicle():
    # "Constructor" function
    def __init__(self, bodystyle):
        self.bodystle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
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
        return f"Driving my {self.enginetype} {self} at {self.speed}"


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
        return f"Driving my {self.enginetype} {self} at {self.speed}"

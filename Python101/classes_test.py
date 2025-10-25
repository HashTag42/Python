import unittest
from classes import Vehicle, Car, Motorcycle
from classes import Sex, Human, Person, Man, Woman
from datetime import date


class Vehicle_Tests(unittest.TestCase):
    def test_tank_Vehicle(self):
        tank = Vehicle("Tank")
        self.assertEqual(str(tank), "Tank")
        self.assertEqual(tank.bodystle, "Tank")
        with self.assertRaises(AttributeError):
            tank.mode
        tank.drive(10)
        self.assertEqual(tank.mode, "driving")
        self.assertEqual(tank.speed, 10)

    def test_gas_Car(self):
        gas_car = Car("gas")
        self.assertEqual(str(gas_car), "Car")
        self.assertEqual(gas_car.bodystle, "Car")
        self.assertEqual(gas_car.enginetype, "gas")
        self.assertEqual(gas_car.doors, 4)
        self.assertEqual(gas_car.wheels, 4)
        self.assertEqual(gas_car.drive(20), "Driving my gas Car at 20")

    def test_gas_sidecar_Motorcycle(self):
        gas_sidecar_mc = Motorcycle("gas", True)
        self.assertEqual(str(gas_sidecar_mc), "Motorcycle")
        self.assertEqual(gas_sidecar_mc.bodystle, "Motorcycle")
        self.assertEqual(gas_sidecar_mc.enginetype, "gas")
        self.assertEqual(gas_sidecar_mc.doors, 0)
        self.assertEqual(gas_sidecar_mc.wheels, 3)
        self.assertEqual(gas_sidecar_mc.drive(30), "Driving my gas Motorcycle at 30")

    def test_electric_Motorcycle(self):
        ev_mc = Motorcycle("electric", False)
        self.assertEqual(str(ev_mc), "Motorcycle")
        self.assertEqual(ev_mc.bodystle, "Motorcycle")
        self.assertEqual(ev_mc.enginetype, "electric")
        self.assertEqual(ev_mc.doors, 0)
        self.assertEqual(ev_mc.wheels, 2)
        self.assertEqual(ev_mc.drive(40), "Driving my electric Motorcycle at 40")


class Human_Tests(unittest.TestCase):
    def test_Human(self):
        female = Human(Sex.FEMALE)
        male = Human(Sex.MALE)
        self.assertEqual(female.sex, Sex.FEMALE)
        self.assertEqual(male.sex, Sex.MALE)

    def test_Human_sex_TypeError(self):
        with self.assertRaises(TypeError):
            Human("Male")

    def test_Human_dob_TypeError(self):
        with self.assertRaises(TypeError):
            Human(Sex.MALE, "today")

    def test_Person_dob(self):
        cesar = Person(Sex.MALE, date(1972, 8, 10), "César")
        self.assertEqual(cesar.dob.year, 1972)
        self.assertEqual(cesar.sex, Sex.MALE)

    def test_Person_dob_TypeError(self):
        with self.assertRaises(TypeError):
            Person("Weird Al", "65")

    def test_Person_age(self):
        name, age = "Fifty", 50
        fifty = Person(Sex.MALE, date(date.today().year - age, 1, 1), name)
        self.assertEqual(fifty.age(), 50)
        self.assertEqual(str(fifty), f"{name} is a {age} years old {fifty.sex.value}.")

    def test_Person_age_Santa(self):
        name, age = "Forty9", 50
        forty9 = Person(Sex.FEMALE, date(date.today().year - age, 12, 31), name)
        self.assertEqual(forty9.age(), age - 1)
        self.assertEqual(str(forty9), f"{name} is a {age - 1} years old {forty9.sex.value}.")

    def test_Man(self):
        mario = Man(date(1971, 1, 1), "Mario")
        self.assertEqual(mario.sex, Sex.MALE)

    def test_Woman(self):
        peach = Woman(date(1981, 12, 31), "Peach")
        self.assertEqual(peach.sex, Sex.FEMALE)

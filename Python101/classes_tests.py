import unittest

from classes import Vehicle, Car, Motorcycle


class classes_Tests(unittest.TestCase):
    def setUp(self):
        pass

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

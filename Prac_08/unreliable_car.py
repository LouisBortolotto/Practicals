"""
CP1404/CP5632 Practical
Car class
"""
from Prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, fuel={}, odometer={}, reliability={}".format(self.name, self.fuel,
                                                 self.odometer, self.reliability)


    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        return distance_driven

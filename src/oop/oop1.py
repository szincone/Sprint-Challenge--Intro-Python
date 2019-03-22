# Write classes for the following class hierarchy:
#
# [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle():
    # it is base
    pass


class GroundVehicle(Vehicle):
    # vehicle base
    pass


class Car(GroundVehicle):
    # groundvehicle base
    pass


class Motorcycle(GroundVehicle):
    # groundvehicle base
    pass


class FlightVehicle(Vehicle):
    # vehicle base
    pass


class Airplane(FlightVehicle):
    # flightvehicle base
    pass


class Starship(FlightVehicle):
    # flightvehicle base
    pass

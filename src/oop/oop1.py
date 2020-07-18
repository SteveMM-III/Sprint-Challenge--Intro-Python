# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
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

#################passing tests

# Base Class - Vehicle
class Vehicle:
    pass


# Vehicle SubClass - GroundVehicle
class GroundVehicle( Vehicle ):
    pass


#GroundVehicle SubClass - Car
class Car( GroundVehicle ):
    pass


#GroundVehicle SubClass - Motorcycle
class Motorcycle( GroundVehicle ):
    pass


#Vehicle SubClass - FlightVehicle
class FlightVehicle( Vehicle ):
    pass


#FlightVehicle SubClass - Airplane
class Airplane( FlightVehicle ):
    pass


#FlightVehicle SubClass - Starship
class Starship( FlightVehicle ):
    pass


################# better examples
'''
# Base Class - Vehicle
class Vehicle:
    def __init__( self, a ):
        self.a = a


# Vehicle SubClass - GroundVehicle
class GroundVehicle( Vehicle ):
    def __init__( self, a, b ):
        super().__init__( a )
        self.b = b


#GroundVehicle SubClass - Car
class Car( GroundVehicle ):
    def __init__( self, a, b, c ):
        super().__init__( a, b )
        self.c = c


#GroundVehicle SubClass - Motorcycle
class Motorcycle( GroundVehicle ):
    def __init__( self, a, b, c ):
        super().__init__( a, b )
        self.c = c


#Vehicle SubClass - FlightVehicle
class FlightVehicle( Vehicle ):
    def __init__( self, a, b ):
        super().__init__( a )
        self.b = b


#FlightVehicle SubClass - Airplane
class Airplane( FlightVehicle ):
    def __init__( self, a, b, c ):
        super().__init__( a, b )
        self.c = c


#FlightVehicle SubClass - Starship
class Starship( FlightVehicle ):
    def __init__( self, a, b, c ):
        super().__init__( a, b )
        self.c = c

'''
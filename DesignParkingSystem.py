# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
# Implement the ParkingSystem class:
#   ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
#   bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkingSpaces = dict()
        self.parkingSpaces[1] = big
        self.parkingSpaces[2] = medium 
        self.parkingSpaces[3] = small

    def addCar(self, carType: int) -> bool:
        if self.parkingSpaces[carType] > 0:
            self.parkingSpaces[carType] -= 1 
            return True 
        return False 

# Test cases
parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))

# An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.
# Implement the UndergroundSystem class:
#   void checkIn(int id, string stationName, int t)
#       A customer with a card ID equal to id, checks in at the station stationName at time t.
#       A customer can only be checked into one place at a time.
#   void checkOut(int id, string stationName, int t)
#       A customer with a card ID equal to id, checks out from the station stationName at time t.
#   double getAverageTime(string startStation, string endStation)
#       Returns the average time it takes to travel from startStation to endStation.
#       The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
#       The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
#       There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
# You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

class UndergroundSystem:
    def __init__(self):
        self.averageTime = dict()
        self.checkedIn = dict()

    def checkIn(self, id, stationName, t):  
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        checkInStation = self.checkedIn[id][0]
        if (checkInStation, stationName) in self.averageTime:
            self.averageTime[(checkInStation, stationName)].append(t - self.checkedIn[id][1])
        else:
            self.averageTime[(checkInStation, stationName)] = [t - self.checkedIn[id][1]]
            
        del self.checkedIn[id]

    def getAverageTime(self, startStation, endStation):
        return sum(self.averageTime[(startStation, endStation)]) / len(self.averageTime[(startStation, endStation)])

# Test cases
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
undergroundSystem.checkIn(10, "Leyton", 24)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))
undergroundSystem.checkOut(10, "Waterloo", 38)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))

undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
print(undergroundSystem.getAverageTime("Leyton", "Paradise"))
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
print(undergroundSystem.getAverageTime("Leyton", "Paradise"))
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
print(undergroundSystem.getAverageTime("Leyton", "Paradise"))
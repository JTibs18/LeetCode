# Design a system that manages the reservation state of n seats that are numbered from 1 to n.
# Implement the SeatManager class:
#   SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
#   int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
#   void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

import heapq

class SeatManager:

    def __init__(self, n: int):
        self.availableSeats = [x for x in range(1,  n + 1)]
        heapq.heapify(self.availableSeats)

    def reserve(self):
        return heapq.heappop(self.availableSeats)

    def unreserve(self, seatNumber: int):
        heapq.heappush(self.availableSeats, seatNumber)

# Test cases
obj = SeatManager(5)
print(obj.reserve())
print(obj.reserve())
obj.unreserve(2)
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
obj.unreserve(5)
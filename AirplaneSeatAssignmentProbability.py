# n passengers board an airplane with exactly n seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:
# Take their own seat if it is still available, and
# Pick other seats randomly when they find their seat occupied
# Return the probability that the nth person gets his own seat.

def nthPersonGetsNthSeat(n): 
    if n == 1: 
        return 1
    return 0.5

# Test cases
n = 1
print(nthPersonGetsNthSeat(n))

n = 2
print(nthPersonGetsNthSeat(n))

n = 3 
print(nthPersonGetsNthSeat(n))

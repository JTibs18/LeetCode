# You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.
# Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.
# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

def minimumTime(time, totalTrips):
    leftPtr = 0 
    rightPtr = time[0] * totalTrips + 1 
    answer = 0 

    while leftPtr < rightPtr - 1: 
        midPtr = (leftPtr + rightPtr) // 2
        trips = 0

        for i in time: 
            trips += midPtr // i 

        if trips < totalTrips: 
            leftPtr = midPtr 
        else: 
            rightPtr = midPtr 
            answer = midPtr
        
    return answer 

# Test cases 
time = [1,2,3]
totalTrips = 5
print(minimumTime(time, totalTrips))

time = [2]
totalTrips = 1
print(minimumTime(time, totalTrips))

time = [5, 10, 10]
totalTrips = 9 
print(minimumTime(time, totalTrips))

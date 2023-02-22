# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Fantastic explanation: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solutions/2934252/capacity-to-ship-packages-within-d-days/

import math

def daysToShip(capacity, weights, days): 
    daysNeeded = 1 
    currentLoad = 0 

    for i in weights: 
        currentLoad += i 

        if currentLoad > capacity: 
            daysNeeded += 1 
            currentLoad = i 
    
    if daysNeeded > days: 
        return False 
        
    return True 

def shipWithinDays(weights, days): 
    maxWeight = max(weights)
    totalWeight = sum(weights)

    while maxWeight < totalWeight: 
        mid = (maxWeight + totalWeight) / 2 

        if daysToShip(mid, weights, days): 
            totalWeight = mid 
        else: 
            maxWeight = mid + 1 
    
    return math.floor(maxWeight)

# Test cases
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights, days))

weights = [3,2,2,4,1,4]
days = 3
print(shipWithinDays(weights, days))

weights = [1,2,3,1,1]
days = 4
print(shipWithinDays(weights, days))

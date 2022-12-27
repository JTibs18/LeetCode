# You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.
# Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

def maximumBags(capacity, rocks, additionalRocks): 
    rockAvailability = []
    fullBags = 0

    for indx, val in enumerate(rocks): 
        if capacity[indx] - val == 0: 
            fullBags += 1 
        else: 
            rockAvailability.append(capacity[indx] - val)
    
    rocksNeeded = sorted(rockAvailability)

    for i in rocksNeeded: 
        if additionalRocks >= i: 
            fullBags += 1 
            additionalRocks = additionalRocks - i 
        else: 
            break 

    return fullBags 

#Test cases 
capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2
print(maximumBags(capacity, rocks, additionalRocks))

capacity = [10,2,2]
rocks = [2,2,0]
additionalRocks = 100
print(maximumBags(capacity, rocks, additionalRocks))

# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.

def numRescueBoats(people, limit): 
    boatCount = 0  
    p1 = 0
    p2 = len(people) - 1 
    people = sorted(people)

    while p1 <= p2: 
        if people[p1] + people[p2] <= limit: 
            p1 += 1 
           
        p2 -= 1 
        boatCount += 1 

    return boatCount 

# Test cases
people = [1,2]
limit = 3
print(numRescueBoats(people, limit))

people = [3,2,2,1]
limit = 3
print(numRescueBoats(people, limit))

people = [3,5,3,4]
limit = 5
print(numRescueBoats(people, limit))

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

def canCompleteCircuit(gas, cost): 
    tank = 0 
    start = 0 
    
    if sum(cost) > sum(gas): 
        return -1
    
    for indx, val in enumerate(gas): 
        tank += val - cost[indx]
        if tank < 0: 
            start = indx + 1 
            tank = 0 

    return start

# Test cases
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas, cost)) 

gas = [2,3,4]
cost = [3,4,3]
print(canCompleteCircuit(gas, cost))  

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(canCompleteCircuit(gas, cost)) 

gas = [2]
cost = [2]
print(canCompleteCircuit(gas, cost)) 

gas = [3,1,1]
cost = [1,2,2]
print(canCompleteCircuit(gas, cost)) 

gas = [1,2,3,4,5,5,70]
cost = [2,3,4,3,9,6,2]
print(canCompleteCircuit(gas, cost))

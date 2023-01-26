# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.

def maximumUnits(boxTypes, truckSize): 
    boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    unitCount = 0 

    for val in boxTypes: 
        if truckSize == 0: 
            break 
        
        if val[0] <= truckSize: 
            unitCount += val[0] * val[1]
            truckSize -= val[0]
        else: 
            unitCount += val[1] * truckSize
            truckSize = 0
    
    return unitCount

# Test case
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(maximumUnits(boxTypes, truckSize))

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(maximumUnits(boxTypes, truckSize))

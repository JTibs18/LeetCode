# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.

def sortPeople(names, heights): 
    heightDict = dict() 
    sortedNames = []

    for indx, val in enumerate(heights): 
        heightDict[val] = names[indx]
    
    heights = sorted(heights, reverse=True)

    for i in heights: 
        sortedNames.append(heightDict[i])
    
    return sortedNames

# Test cases 
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(sortPeople(names, heights))

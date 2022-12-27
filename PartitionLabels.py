# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

def partitionLabels(s): 
    letterIndex = dict()
    sizeOfPartition = []
    rangeStart = 0 
    ptr1 = 0
    ptr2 = 0

    for indx, val in enumerate(s): 
        if val in letterIndex: 
            letterIndex[val].append(indx)
        else: 
            letterIndex[val] = [indx]

    while ptr2 != len(s) - 1: 
        if letterIndex[s[ptr1]][-1] > ptr2: 
            ptr2 = letterIndex[s[ptr1]][-1]
        
        if ptr1 == ptr2: 
            sizeOfPartition.append((ptr2 - rangeStart) + 1)
            ptr1 += 1 
            rangeStart = ptr1
        else:
            ptr1 += 1 
    
    if (ptr2 - rangeStart) + 1 != 0: 
        sizeOfPartition.append((ptr2 - rangeStart) + 1)
    return sizeOfPartition

# Test cases
s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))

s = "eccbbbbdec"
print(partitionLabels(s))

s = "caedbdedda"
print(partitionLabels(s))

s = "eaaaabaaec"
print(partitionLabels(s))

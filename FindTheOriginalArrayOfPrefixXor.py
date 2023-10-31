# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.
# It can be proven that the answer is unique.

def findArray(pref): 
    currentXor = 0
    runningXor = 0 
    newArray = []

    for i in pref: 
        currentXor = runningXor ^ i
        runningXor ^= currentXor
        newArray.append(currentXor)
    
    return newArray

# Test cases 
pref = [5,2,0,3,1]
print(findArray(pref))

pref = [13]
print(findArray(pref))

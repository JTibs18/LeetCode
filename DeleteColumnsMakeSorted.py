# You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

def minDeletionSize(strs): 
    colDict = dict() 
    delColumn = 0

    for i in strs: 
        for indx, letter in enumerate(i): 
            if indx in colDict: 
                colDict[indx].append(letter)
            else: 
                colDict[indx] = [letter]
    
    for value in colDict.values(): 
        if sorted(value) != value: 
            delColumn += 1 
    
    return delColumn

# Test cases
strs = ["cba","daf","ghi"]
print(minDeletionSize(strs))

strs = ["a","b"]
print(minDeletionSize(strs))

strs = ["zyx","wvu","tsr"]
print(minDeletionSize(strs))

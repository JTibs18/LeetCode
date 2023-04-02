# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

def successfulPairs(spells, potions, success):
    potions = sorted(potions, reverse=True) 
    successfulPairs = []

    for i in spells: 
        l = 0 
        r = len(potions)

        while l < r: 
            mid = (l + r) // 2 
            if potions[mid] * i >= success: 
                l = mid + 1
            else: 
                r = mid 
        
        successfulPairs.append(l)
 
    return successfulPairs

# Test cases
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells, potions, success))

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(successfulPairs(spells, potions, success))


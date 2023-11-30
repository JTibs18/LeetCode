# RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.
# Implement the RandomizedCollection class:
#   RandomizedCollection() Initializes the empty RandomizedCollection object.
#   bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
#   bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
#   int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of the same values the multiset contains.
# You must implement the functions of the class such that each function works on average O(1) time complexity.
# Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.

from random import sample

# very slow runtime, great memory efficiency 
class RandomizedCollection1:
    def __init__(self):
        self.randomCollection = []

    def insert(self, val):
        returnVal = True

        if val in self.randomCollection: 
            returnVal = False 
        
        self.randomCollection.append(val)
        return returnVal 

    def remove(self, val): 
        if val in self.randomCollection:
            self.randomCollection.remove(val)
            return True 
        return False 
    
    def getRandom(self):
        return sample(self.randomCollection, 1)[0]
    
# faster runtime, takes more memory 
class RandomizedCollection:
    def __init__(self):
        self.randomCollection = []
        self.randomMap = dict()

    def insert(self, val):
        self.randomCollection.append(val)
        
        if val in self.randomMap: 
            self.randomMap[val] += 1
            return False         
        
        self.randomMap[val] = 1 
        return True 

    def remove(self, val): 
        if val in self.randomMap:
            self.randomCollection.remove(val)
            self.randomMap[val] -= 1
            if self.randomMap[val] == 0:
                del self.randomMap[val]
            return True 
        return False 
    
    def getRandom(self):
        return sample(self.randomCollection, 1)[0]

# Test cases
randomizedCollection = RandomizedCollection()
print(randomizedCollection.insert(1))
print(randomizedCollection.insert(1))
print(randomizedCollection.insert(2))
print(randomizedCollection.getRandom())
print(randomizedCollection.remove(1))
print(randomizedCollection.getRandom())
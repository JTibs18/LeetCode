# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
# Solved with help from https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/2858286/python3-hashmap-list-got-this-in-google-phone-interview/?envType=study-plan-v2&envId=top-interview-150

import random 

class RandomizedSet: 

    def __init__(self): 
        self.indices = dict()
        self.array = []

    def insert(self, val) -> bool:
        if val not in self.indices:
            self.array.append(val)
            self.indices[val] = len(self.array) - 1  
            return True
        return False 

    def remove(self, val) -> bool:
        if val not in self.indices: 
            return False 
        
        index = self.indices[val]

        self.indices[self.array[-1]] = index 
        self.array[index] = self.array[-1]

        self.indices.pop(val)
        self.array.pop()
        return True 

    def getRandom(self): 
        return random.choice(self.array)

# Test case 
obj = RandomizedSet()
param_1 = obj.insert(1)
print(param_1)
param_2 = obj.remove(2)
print(param_2)
param_3 = obj.insert(2)
print(param_3)
param_4 = obj.getRandom()
print(param_4)
param_5 = obj.remove(1)
print(param_5)
param_6 = obj.insert(2)
print(param_6)
param_7 = obj.getRandom()
print(param_7)
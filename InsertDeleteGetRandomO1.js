// Implement the RandomizedSet class:
//  RandomizedSet() Initializes the RandomizedSet object.
//  bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
//  bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
//  int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
// You must implement the functions of the class such that each function works in average O(1) time complexity.

var RandomizedSet = function() {
    rSet = [];  
};

RandomizedSet.prototype.insert = function(val) {
    if (rSet.includes(val)){
        return false
    } 

    rSet.push(val)
    return true
};

RandomizedSet.prototype.remove = function(val) {
    if (rSet.includes(val)){
        rSet.splice(rSet.indexOf(val), 1)
        return true
    }
    return false
};

RandomizedSet.prototype.getRandom = function() {
    return rSet[Math.floor(Math.random() * rSet.length)]
};

// Test case
var randomizedSet = new RandomizedSet()
console.log(randomizedSet.insert(1))
console.log(randomizedSet.remove(2))
console.log(randomizedSet.insert(2))
console.log(randomizedSet.getRandom())
console.log(randomizedSet.remove(1))
console.log(randomizedSet.insert(2))
console.log(randomizedSet.getRandom())

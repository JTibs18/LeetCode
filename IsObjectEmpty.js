// Given an object or an array, return if it is empty.
//   An empty object contains no key-value pairs.
//   An empty array contains no elements.
// You may assume the object or array is the output of JSON.parse.

function isEmpty(obj){
    return Object.keys(obj).length ? false : true; 
};

// Test cases
obj = {"x": 5, "y": 42}
console.log(isEmpty(obj))

obj = {}
console.log(isEmpty(obj))

obj = [null, false, 0]
console.log(isEmpty(obj))

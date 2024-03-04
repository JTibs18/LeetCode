// Write code that enhances all arrays such that you can call the array.last() method on any array and it will return the last element. If there are no elements in the array, it should return -1.
// You may assume the array is the output of JSON.parse.

declare global {
    interface Array<T> {
        last(): T | -1;
    }
}

Array.prototype.last = function() {
    return this.length ? this[this.length - 1] : -1; 
};  

export {};

// Test cases
let arr = [null, {}, 3];
console.log(arr.last());

arr = []
console.log(arr.last())
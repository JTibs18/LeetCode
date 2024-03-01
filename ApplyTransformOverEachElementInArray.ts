// Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.
// The returned array should be created such that returnedArray[i] = fn(arr[i], i).
// Please solve it without the built-in Array.map method.

function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    for (var i = 0; i < arr.length; i++){
        arr[i] = fn(arr[i], i); 
    };

    return arr;
};

// Test cases
var arr = [1,2,3]
var fn = function plusone(n: number) { return n + 1; }
console.log(map(arr, fn))

arr = [1,2,3]
var fn1 = function plusI(n:number, i:number) { return n + i; }
console.log(map(arr, fn1))

arr = [10,20,30]
var fn2 = function constant() { return 42; }
console.log(map(arr, fn2))

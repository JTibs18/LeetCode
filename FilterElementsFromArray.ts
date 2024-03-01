// Given an integer array arr and a filtering function fn, return a filtered array filteredArr.
// The fn function takes one or two arguments:
// arr[i] - number from the arr
// i - index of arr[i]
// filteredArr should only contain the elements from the arr for which the expression fn(arr[i], i) evaluates to a truthy value. A truthy value is a value where Boolean(value) returns true.
// Please solve it without the built-in Array.filter method.

type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[]{
    var newArr:number[] = [];

    for (var i = 0; i < arr.length; i++){
        if (fn(arr[i], i)){
            newArr.push(arr[i]);
        };
    };

    return newArr;
};

// Test cases
var arr = [0, 10, 20, 30]
const f = function greaterThan10(n: number) {return n > 10; }
console.log(filter(arr, f))

arr = [1, 2, 3]
const f2 = function firstIndex(n:number, i:number) { return i === 0; }
console.log(filter(arr, f2))

arr = [-2, -1, 0, 1, 2]
const f3 = function plusOne(n:number) { return n + 1}
console.log(filter(arr, f3)) 
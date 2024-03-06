// Given an array arr and a function fn, return a sorted array sortedArr. You can assume fn only returns numbers and those numbers determine the sort order of sortedArr. sortedArray must be sorted in ascending order by fn output.
// You may assume that fn will never duplicate numbers for a given array.

type JSONValue1 = boolean | number | string | JSONValue1[] | { [key: string]: JSONValue1 };
type Fn1 = (value: JSONValue1) => number

function sortBy(arr: JSONValue1[], fn: Fn1): JSONValue1[] {
    return arr.sort((a, b) => fn(a) - fn(b)) 
};

// Test case
console.log(sortBy([5, 4, 1, 2, 3], (x: JSONValue1): number => Number(x)))
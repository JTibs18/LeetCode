// Given an array arr and a chunk size size, return a chunked array. A chunked array contains the original elements in arr, but consists of subarrays each of length size. The length of the last subarray may be less than size if arr.length is not evenly divisible by size.
// You may assume the array is the output of JSON.parse. In other words, it is valid JSON.
// Please solve it without using lodash's _.chunk function.

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    let newArr: Obj[][] = []; 

    for (let i = 0; i < arr.length; i = i + size){
        newArr.push(arr.slice(i, i + size));
    };

    return newArr;
};

// Test cases
let arr = "[1, 2, 3, 4, 5]";
let size = 1;
console.log(chunk(JSON.parse(arr), size));

arr = "[1, 9, 6, 3, 2]";
size = 3;
console.log(chunk(JSON.parse(arr), size));

arr = "[8, 5, 3, 2, 6]";
size = 6;
console.log(chunk(JSON.parse(arr), size));

arr = "[]";
size = 1;
console.log(chunk(JSON.parse(arr), size));

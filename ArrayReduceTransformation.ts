// Given an integer array nums, a reducer function fn, and an initial value init, return the final result obtained by executing the fn function on each element of the array, sequentially, passing in the return value from the calculation on the preceding element.
// This result is achieved through the following operations: val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ... until every element in the array has been processed. The ultimate value of val is then returned.
// If the length of the array is 0, the function should return init.
// Please solve it without using the built-in Array.reduce method.

type Fn = (accum: number, curr: number) => number

function reduce1(nums: number[], fn: Fn, init:number): number {
    for (var i = 0; i < nums.length; i ++){
        init = fn(init, nums[i]);
    }; 
    
    return init;
};

function reduce(nums: number[], fn: Fn, init:number): number {
    nums.forEach(element => init = fn(init, element));
    return init;
};


// Test cases
var nums = [1, 2, 3, 4]
var func = function sum(accum: number, curr: number) { return accum + curr; }
var init = 0
console.log(reduce(nums, func, init))
 
nums = [1, 2, 3, 4]
var func2 = function sum(accum: number, curr: number) { return accum + curr * curr; }
var init = 100
console.log(reduce(nums, func2, init))

nums = []
var func3 = function sum(accum: number, curr: number) { return 0; }
init = 25
console.log(reduce(nums, func3, init))
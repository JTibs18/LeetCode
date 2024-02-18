// Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
// Return the selected integer.

function findNonMinOrMax(nums){
    if (nums.length < 3){
        return -1;
    };
    return nums.sort((x, y) => x - y)[1];
};

// Test cases
nums = [3, 2, 1, 4]
console.log(findNonMinOrMax(nums))

nums = [1, 2]
console.log(findNonMinOrMax(nums))

nums = [2, 1, 3]
console.log(findNonMinOrMax(nums))

// You are given an integer array nums of size n and a positive integer k.
// Divide the array into one or more arrays of size 3 satisfying the following conditions:
//  Each element of nums should be in exactly one array.
//  The difference between any two elements in one array is less than or equal to k.
// Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

function divideArray(nums, k){
    arr = [];
    curArr = [];
    nums.sort(function(a, b){return a-b});

    for (i = 0; i < nums.length; i++){
        if (curArr.length == 0 || Math.abs(curArr[0] - nums[i]) <= k ){
            curArr.push(nums[i]);
        }else{
            return [];
        };

        if (curArr.length == 3){
            arr.push(curArr);
            curArr = [];
        };
    };

    return arr;
};

// Test cases
nums = [1,3,4,8,7,9,3,5,1]
k = 2
console.log(divideArray(nums, k))

nums = [1,3,3,2,7,3]
k = 3
console.log(divideArray(nums, k))


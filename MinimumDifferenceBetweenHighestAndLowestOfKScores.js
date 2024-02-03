// You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
// Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
// Return the minimum possible difference.

function minimumDifference(nums, k){
    nums.sort((a, b) => a - b);
    minDiff = Infinity;

    for (i = 0; i < nums.length - k + 1; i++){
        minDiff = Math.min(nums[i + k - 1] - nums[i], minDiff);
    };

    return minDiff;
}; 

// Test cases
nums = [90]
k = 1
console.log(minimumDifference(nums, k))

nums = [9, 4, 1, 7]
k = 2
console.log(minimumDifference(nums, k))

nums = [87063,61094,44530,21297,95857,93551,9918]
k = 6
console.log(minimumDifference(nums, k))

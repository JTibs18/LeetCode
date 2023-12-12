// Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

function maxProduct(nums){
    nums.sort(function(a, b) {return a - b;}).reverse();
    return (nums[0] - 1) * (nums[1] - 1);
};

nums = [3, 4, 5, 2];
console.log(maxProduct(nums));

nums = [1, 5, 4, 5];
console.log(maxProduct(nums));

nums = [3, 7];
console.log(maxProduct(nums));

nums = [10, 2, 5, 2];
console.log(maxProduct(nums));

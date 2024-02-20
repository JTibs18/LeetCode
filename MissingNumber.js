// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

function missingNumber(nums){
    for (i = 0; i < nums.length + 1; i++){
        if (!(nums.includes(i))){
            return i;
        };
    };
};

// Test cases
nums = [3, 0, 1]
console.log(missingNumber(nums))

nums = [0, 1]
console.log(missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
console.log(missingNumber(nums))

// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

function majorityElement(nums){
    maxNumCount = 0;
    maxNum = -1;
    localMax = 0;
    curNum = -1;

    nums
    .sort((a, b) => {return a - b})
    .forEach(x => {
        if (curNum != x){
            if (maxNumCount < localMax){
                maxNum = curNum; 
                maxNumCount = localMax;
            }
            localMax = 1;
            curNum = x; 
        }else{
            localMax += 1;
        }
    });

    if (maxNumCount < localMax){
        maxNum = curNum;
        maxNumCount = localMax;
    }; 
    
    return maxNum;
};

// Test cases
nums = [3, 2, 3]
console.log(majorityElement(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
console.log(majorityElement(nums))

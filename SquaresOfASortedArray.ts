// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

function sortedSquares1(nums: number[]): number[]{
    for (var i = 0; i < nums.length; i++){
        nums[i] = nums[i] ** 2
    }; 

    nums.sort((a, b) => a - b);
    return nums;
}; 

// Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

function sortedSquares(nums: number[]): number[]{
    var ptr1 = 0;
    var ptr2 = nums.length - 1; 
    var newArr: number[] = [];

    while (ptr1 <= ptr2){
        if (Math.abs(nums[ptr1]) < Math.abs(nums[ptr2])){
            newArr.push(nums[ptr2] ** 2);
            ptr2 -= 1;
        }else{
            newArr.push(nums[ptr1] ** 2);
            ptr1 += 1; 
        };
    };
    
    return newArr.reverse();
};

// Test cases
var nums = [-4, -1, 0, 3, 10]
console.log(sortedSquares(nums))

nums = [-7, -3, 2, 3, 11]
console.log(sortedSquares(nums))

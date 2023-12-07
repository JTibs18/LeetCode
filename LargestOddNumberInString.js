// You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
// A substring is a contiguous sequence of characters within a string.

function largestOddNumber(num){
    for (let i = num.length - 1; i >= 0; i--){
        if (parseInt(num[i]) % 2 != 0){
            return num.substring(0, i + 1);
        };
    };
    return '';
}; 

num = '52'
console.log(largestOddNumber(num))

num = "4206"
console.log(largestOddNumber(num))

num = "35427"
console.log(largestOddNumber(num))

num = "239537672423884969653287101"
console.log(largestOddNumber(num))

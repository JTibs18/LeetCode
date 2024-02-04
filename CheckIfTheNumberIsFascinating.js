// You are given an integer n that consists of exactly 3 digits.
// We call the number n fascinating if, after the following modification, the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0's:
//  Concatenate n with the numbers 2 * n and 3 * n.
// Return true if n is fascinating, or false otherwise.
// Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

function isFascinating(n){
    newNum = Array.from(String(n), Number).concat(Array.from(String(n * 2), Number)).concat(Array.from(String(n * 3), Number)).sort();
    
    for (i = 0; i < newNum.length; i++){
        if (i + 1 != newNum[i]){
            return false; 
        };
    };

    return true;
}; 

// Test cases 
n = 192
console.log(isFascinating(n))

n = 100 
console.log(isFascinating(n))

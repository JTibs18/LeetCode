// Given an integer n, return true if it is a power of two. Otherwise, return false.
// An integer n is a power of two, if there exists an integer x such that n == 2x.

function isPowerOfTwo(n){
    return n ? 2 ** Math.round(Math.log(n) / Math.log(2)) == n : false;
}; 

// Test cases
n = 1 
console.log(isPowerOfTwo(n))

n = 16
console.log(isPowerOfTwo(n))

n = 3
console.log(isPowerOfTwo(n))

n = 8 
console.log(isPowerOfTwo(n))

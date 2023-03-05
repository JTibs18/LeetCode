// Given an integer number n, return the difference between the product of its digits and the sum of its digits.

function subtractProductAndSum(n){
    var n = String(n).split('').map(Number);
    var sum = n.reduce((num, a) => Number(num) + a);
    var multi = n.reduce((num, m) => m * num, 1);
    return multi - sum;
}

// Test cases
n = 234
console.log(subtractProductAndSum(n))

n = 4421
console.log(subtractProductAndSum(n))

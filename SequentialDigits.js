// An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
// Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

function sequentialDigits(low, high){
    possibleNums = "123456789";
    seqDigits = [];

    for (i = low.toString().length; i < high.toString().length + 1; i++){
        ptr = 0;

        while (ptr + i <= possibleNums.length){
            newNum = parseInt(possibleNums.slice(ptr, ptr + i));

            if (newNum >= low && newNum <= high){
                seqDigits.push(newNum);
            };
            ptr += 1;
        };
    };

    return seqDigits;
}; 

// Test cases
low = 100
high = 300
console.log(sequentialDigits(low, high))

low = 1000
high = 13000
console.log(sequentialDigits(low, high))

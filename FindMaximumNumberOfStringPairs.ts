// You are given a 0-indexed array words consisting of distinct strings.
// The string words[i] can be paired with the string words[j] if:
//  The string words[i] is equal to the reversed string of words[j].
//  0 <= i < j < words.length.
// Return the maximum number of pairs that can be formed from the array words.
// Note that each string can belong in at most one pair.

function maximumNumberOfStringPairs1(words: string[]): number {
    words = words.map(x => x.split("").sort().join(""))
    var count = 0 

    while (words.length){
        if (words.includes(words.pop()!)){
            count += 1; 
        };
    };

    return count;
}; 

// using set
function maximumNumberOfStringPairs(words: string[]): number {
    var count = 0;
    var pairCount = new Set();

    for (var i of words.map(x => x.split("").sort().join(""))){
        if (pairCount.has(i)){
            count += 1;
        }else{
            pairCount.add(i);
        };
    };

    return count;
}; 

// Test cases
var words: string[] = ["cd","ac","dc","ca","zz"]
console.log(maximumNumberOfStringPairs(words))

var words: string[]  = ["ab","ba","cc"]
console.log(maximumNumberOfStringPairs(words))

var words: string[]  = ["aa","ab"]
console.log(maximumNumberOfStringPairs(words))

// Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
// Return the sorted string. If there are multiple answers, return any of them.

function frequencySort(s){
    characterCount = {}

    for (const i of s){
        if (i in characterCount){
            characterCount[i] += 1;
        }else{
            characterCount[i] = 1;
        };
    };

    return Object.entries(characterCount)
        .sort((x, y) => {
            return y[1] - x[1];
        })
        .map((e) => {
            return e[0].repeat(e[1]);
        })
        .join("");
}; 

// Test cases
s = "tree"
console.log(frequencySort(s))

s = "cccaaa"
console.log(frequencySort(s))

s = "Aabb"
console.log(frequencySort(s))

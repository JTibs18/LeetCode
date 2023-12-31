// Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
// A substring is a contiguous sequence of characters within a string.

function maxLengthBetweenEqualCharacter(s){
    charIndx = {}
    maxLen = -1

    for(i = 0; i < s.length; i++){
        if (s[i] in charIndx){
            charIndx[s[i]].push(i)
        }else{
            charIndx[s[i]] = [i]
        }
    }

    for (value of Object.values(charIndx)){
        maxLen = Math.max(value[value.length - 1] - value[0] - 1, maxLen)
    }

    return maxLen
}; 

// Test cases
s = "aa"
console.log(maxLengthBetweenEqualCharacter(s))

s = "abca"
console.log(maxLengthBetweenEqualCharacter(s))

s = "cbzxy"
console.log(maxLengthBetweenEqualCharacter(s))

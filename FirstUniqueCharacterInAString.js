// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

function firstUniqChar(s){
    charCount = {}

    for (i = 0; i < s.length; i++){
        if (s[i] in charCount){
            charCount[s[i]].push(i);
        }else{
            charCount[s[i]] = [i];
        };
    };

    for (value of Object.values(charCount)){
        if (value.length == 1){
            return value[0];
        };
    };

    return -1;
}; 


// Test cases
s = "leetcode"
console.log(firstUniqChar(s))

s = 'loveleetcode'
console.log(firstUniqChar(s))

s = "aabb"
console.log(firstUniqChar(s))
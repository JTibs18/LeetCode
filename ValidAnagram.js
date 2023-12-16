// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

function isAnagram(s, t){
    sLetters = {};
    tLetters = {};

    if (new Set(s).size != new Set(t).size){
        return false; 
    }

    for (i = 0; i < s.length; i++){
        if (s[i] in sLetters){
            sLetters[s[i]] += 1;
        }else{
            sLetters[s[i]] = 1;
        }
    }

    for (i = 0; i < t.length; i++){
        if (t[i] in tLetters){
            tLetters[t[i]] += 1;
        }else{
            tLetters[t[i]] = 1;
        }
    }

    for ([key, val] of Object.entries(sLetters)){
        if (!(key in tLetters) || (tLetters[key] != val)){
            return false;
        }
    }
    return true;
}

// Test cases
s = "anagram"
t = "nagaram"
console.log(isAnagram(s, t))

s = "rat"
t = "car"
console.log(isAnagram(s, t))

s = "a"
t = "ab"
console.log(isAnagram(s, t))

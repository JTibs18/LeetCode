// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

function strStr(haystack, needle){
    var ptr1 = 0 
    var ptr2 = needle.length

    while (ptr2 <= haystack.length){
        if (needle == haystack.slice(ptr1, ptr2)){
            return ptr1 
        }
        ptr1 += 1 
        ptr2 += 1 
    }
    return -1 
};

// Test cases 
haystack = "sadbutsad"
needle = "sad"
console.log(strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
console.log(strStr(haystack, needle))

haystack = "a"
needle = "a"
console.log(strStr(haystack, needle))
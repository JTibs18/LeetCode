// Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
// A string is palindromic if it reads the same forward and backward.

function firstPalindrome(words){
    for (w of words){
        ptr1 = 0;
        ptr2 = w.length - 1;

        while (ptr1 <= ptr2){
            if (w[ptr1] != w[ptr2]){
                break; 
            };

            ptr1 += 1; 
            ptr2 -= 1;
        };

        if (ptr1 >= ptr2){
            return w;
        };
    };

    return "";
};

// Test cases
words = ["abc","car","ada","racecar","cool"]
console.log(firstPalindrome(words))

words = ["notapalindrome","racecar"]
console.log(firstPalindrome(words))

words = ["def","ghi"]
console.log(firstPalindrome(words))

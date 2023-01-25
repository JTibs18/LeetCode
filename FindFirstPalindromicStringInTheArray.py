# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

def firstPalindrome(words):
    for word in words:
        ptr1 = 0
        ptr2 = len(word) - 1 
        foundPalindrome = True 

        while ptr1 <= ptr2: 
            if word[ptr1] != word[ptr2]: 
                foundPalindrome = False 
                break 

            ptr1 += 1 
            ptr2 -= 1

        if foundPalindrome == True: 
            return word 
    
    return ''

# Test cases
words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))

words = ["notapalindrome","racecar"]
print(firstPalindrome(words))

words = ["def","ghi"]
print(firstPalindrome(words))

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(s): 
    reversed = ''
    s = s.split(" ")

    for i in s: 
        reversed += i[::-1] + ' '

    return reversed.strip()

# Test cases
s = "Let's take LeetCode contest"
print(reverseWords(s))

s = "God Ding"
print(reverseWords(s))

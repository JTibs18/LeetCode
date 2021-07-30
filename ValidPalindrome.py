# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def isPalindrome(s):
    newS = ""

    for char in s:
        if char != " " and char != "," and char != ":" and char != "." and char != "@" and char != "#" and char != "_" and char != "\"" and char != "[" and char != "]" and char != "/" and char != "{" and char != "}" and char != '"' and char != "'" and char != "-" and char != "?" and char != "!" and char != ";" and char != "(" and char != ")" and char != "`": 
            newS += char
    if newS.lower() == newS[::-1].lower():
        return True
    else:
        return False

#Test Cases
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

s = "race a car"
print(isPalindrome(s))

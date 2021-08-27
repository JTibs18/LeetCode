# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    ss = dict()
    st = dict()

    for i in s:
        if i not in ss:
            ss[i] = 1
        else:
            ss[i] += 1

    for i in t:
        if i not in st:
            st[i] = 1
        else:
            st[i] += 1

    return st == ss

#Slower Solution, a little more space efficient
def isAnagram2 (s, t):
    if len(s) != len(t):
        return False

    for val in s:
        if val in t:
            t = t.replace(val, "" ,1)
        else:
            return False
    return True

#Test cases
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
print(isAnagram2(s, t))

s = "rat"
t = "car"
print(isAnagram(s, t))
print(isAnagram2(s, t))

s = "aa"
t = "a"
print(isAnagram(s, t))
print(isAnagram2(s, t))

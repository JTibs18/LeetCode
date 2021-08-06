# Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

def frequencySort(s):
    freq = dict()
    ans = ""

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    val = sorted(freq.items(), key = lambda x:x[1], reverse=True)

    for i in val:
        ans = ans + (i[0] * i[1])

    return ans
    
#Test Cases
s = "tree"
print(frequencySort(s))

s = "cccaaa"
print(frequencySort(s))

s = "Aabb"
print(frequencySort(s))

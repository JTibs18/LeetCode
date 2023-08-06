# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

def reverseWords1(s): 
    words = s.split(" ")
    output = ""

    for indx in range(len(words) - 1, -1, -1):
        val = words[indx].strip()

        if val != "": 
            output += val + " "

    return output.strip()

# faster algorithm, same memory usage
def reverseWords(s): 
    words = s.split(" ")
    ptr1 = 0 
    ptr2 = len(words) - 1

    while ptr1 < ptr2: 
        firstWord = words[ptr1].strip()
        secondWord = words[ptr2].strip()

        if firstWord != "" and secondWord != "": 
            words[ptr1] = secondWord
            words[ptr2] = firstWord 

            ptr1 += 1
            ptr2 -= 1 
        else: 
            if secondWord == "":
                words.pop(ptr2) 
                ptr2 -= 1 
            if firstWord == "": 
                words.pop(ptr1)
                ptr2 -= 1

    if ptr1 == ptr2 and words[ptr1].strip() == "": 
        words.pop(ptr1)
              
    return " ".join(words)

# Test cases
s = "the sky is blue"
print(reverseWords(s))

s = "  hello world  "
print(reverseWords(s))

s = "a good   example"
print(reverseWords(s))

s = " 3c      2zPeO dpIMVv2SG    1AM       o       VnUhxK a5YKNyuG     x9    EQ  ruJO       0Dtb8qG91w 1rT3zH F0m n G wU"
print(reverseWords(s))

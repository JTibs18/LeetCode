# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
# Return the lexicographically largest repeatLimitedString possible.
# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

# For weekly contest 281.

def repeatLimitedString(s, repeatLimit):
    charCount = {}
    uniqueChars = []
    output = ""
    extraLetter = True

    for i in s:
        if i in charCount:
            charCount[i] += 1
        else:
            charCount[i] = 1
            uniqueChars.append(i)
    uniqueChars.sort(reverse=True)

    for indx, val in enumerate(uniqueChars):
        while (charCount.get(val) > repeatLimit):
            charCount[val] = charCount.get(val) - repeatLimit
            output += val * repeatLimit
            if indx + 1 < len(uniqueChars):
                output += uniqueChars[indx + 1]
                charCount[uniqueChars[indx + 1]] = charCount.get(uniqueChars[indx + 1]) - 1
            else:
                extraLetter = False
                break

        if charCount.get(val) > 0 and extraLetter == True:
            output += charCount.get(val) * val

    return output

#Test Cases
s = "cczazcc"
repeatLimit = 3
print(repeatLimitedString(s, repeatLimit))

s = "aababab"
repeatLimit = 2
print(repeatLimitedString(s, repeatLimit))

s = "xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt"
repeatLimit = 1
print(repeatLimitedString(s, repeatLimit))

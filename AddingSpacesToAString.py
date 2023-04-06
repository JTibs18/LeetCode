# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

def addSpaces(s, spaces): 
    newString = ""
    spacesPtr = 0

    for indx, val in enumerate(s):
        if spacesPtr < len(spaces) and indx == spaces[spacesPtr]: 
            spacesPtr += 1 
            newString += " " + val 
        else: 
            newString += val 

    return newString

# Test cases
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(addSpaces(s, spaces))

s = "icodeinpython"
spaces = [1,5,7,9]
print(addSpaces(s, spaces))

s = "spacing"
spaces = [0,1,2,3,4,5,6]
print(addSpaces(s, spaces))

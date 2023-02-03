# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

def convert(s, numRows): 
    add = True 
    indx = 0
    output = ['' for x in range(numRows)]
    convertedOutput = ''

    if numRows == 1: 
        return s

    for i in s: 
        if indx == numRows - 1: 
            add = False 
        elif indx == 0: 
            add = True 

        output[indx] = output[indx] + i 

        if add == True: 
            indx += 1 
        else: 
            indx -= 1
    
    for i in output: 
        convertedOutput += i 

    return convertedOutput

# Test cases
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))

s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))

s = "A"
numRows = 1
print(convert(s, numRows))

s = "ABC"
numRows = 1
print(convert(s, numRows))

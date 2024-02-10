# You are given a string s and two integers x and y. You can perform two types of operations any number of times.
#   Remove substring "ab" and gain x points.
#       For example, when removing "ab" from "cabxbae" it becomes "cxbae".
#   Remove substring "ba" and gain y points.
#   For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

def maximumGain(s, x, y):
    points = 0

    if x > y:
        removeOrder = [["ab", x], ["ba", y]]
    else:
        removeOrder = [["ba", y], ["ab", x]]

    for substring, p in removeOrder:
        stack = []

        for i in s:
            if stack and i == substring[1] and stack[-1] == substring[0]:
                stack.pop()
                points += p 
            else:
                stack.append(i)

        s = stack

    return points        

# Test cases
s = "cdbcbbaaabab"
x = 4
y = 5
print(maximumGain(s, x, y))

s = "aabbaaxybbaabb"
x = 5
y = 4
print(maximumGain(s, x, y))

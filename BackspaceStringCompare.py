# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

def backspaceCompare(s, t):
    sStack = []
    tStack = []
    for indx, value in enumerate(s):
        if value == "#" and len(sStack) != 0:
            sStack.pop()
        elif value != "#":
            sStack.append(value)
    for indx, value in enumerate(t):
        if value == "#" and len(tStack) != 0:
            tStack.pop()
        elif value != "#": 
            tStack.append(value)
    return (sStack == tStack)

#Test cases
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))

s = "ab##"
t = "c#d#"
print(backspaceCompare(s, t))

s = "a##c"
t = "#a#c"
print(backspaceCompare(s, t))

s = "a#c"
t = "b"
print(backspaceCompare(s, t))

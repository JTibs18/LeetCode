# Your friend is typing his name into a keyboard.
# Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

# EXAMPLE #1
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.

# EXAMPLE #2
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

# EXAMPLE #3
# Input: name = "leelee", typed = "lleeelee"
# Output: true

# EXAMPLE #4
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.

def longPressed(name, typed):
    p = 0
    for index, value in enumerate(typed):
        if (len(name) > len(typed)):
            return False
        if (p < len(name) and value == name[p]):
            p += 1
        elif (index == 0 or value != typed[index - 1]):
            return False
    if (p == (len(name))):
        return True
    else:
        return False

#Test cases
name = "alex"
typed = "aaleex"
print(longPressed(name, typed))

name = "saeed"
typed = "ssaaedd"
print(longPressed(name, typed))

name = "leelee"
typed = "lleeelee"
print(longPressed(name, typed))

name = "laiden"
typed = "laiden"
print(longPressed(name, typed))

name = "vtkgn"
typed = "vttkgnn"
print(longPressed(name, typed))

name = "a"
typed = "b"
print(longPressed(name, typed))

name = "alexd"
typed = "ale"
print(longPressed(name, typed))

name = "pyplrz"
typed = "ppyypllr"
print(longPressed(name, typed))

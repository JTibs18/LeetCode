# Given two integer arrays of equal length target and arr.
# In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.
# Return True if you can make arr equal to target, or False otherwise.

# Faster but less memory efficient
def canBeEqual(target, arr):
    for i in arr:
        if i not in target:
            return False
        target.remove(i)
    return True

# More memory efficient but slower 
def canBeEqual2(target, arr):
    return sorted(target) == sorted(arr)

#Test cases
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(canBeEqual2(target, arr))
print(canBeEqual(target, arr))

target = [7]
arr = [7]
print(canBeEqual2(target, arr))
print(canBeEqual(target, arr))

target = [1, 12]
arr = [12, 1]
print(canBeEqual2(target, arr))
print(canBeEqual(target, arr))

target = [3, 7, 9]
arr = [3, 7, 11]
print(canBeEqual2(target, arr))
print(canBeEqual(target, arr))

target = [1,1,1,1,1]
arr = [1,1,1,1,1]
print(canBeEqual2(target, arr))
print(canBeEqual(target, arr))

target = [1,2,2,3]
arr = [1,1,2,3]
print(canBeEqual2(target, arr))
print(canBeEqual(target, arr))

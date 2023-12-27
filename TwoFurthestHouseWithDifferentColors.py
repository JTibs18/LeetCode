# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.
# Return the maximum distance between two houses with different colors.
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

# naive solution
def maxDistance1(colors):
    ptr1 = 0
    ptr2 = len(colors) - 1

    while ptr1 < len(colors): 
        if colors[ptr1] != colors[-1]:
            break
        ptr1 += 1
    
    while ptr2 >= 0:
        if colors[ptr2] != colors[0]:
            break
        ptr2 -= 1

    return max(len(colors) - ptr1 - 1, ptr2)

# faster and more space efficient solution 
def maxDistance(colors):
    ptr1 = 0
    ptr2 = len(colors) - 1

    while ptr1 < len(colors):
        if colors[ptr1] != colors[-1]:
            return len(colors) - 1 - ptr1 
        
        if colors[ptr2] != colors[0]:
            return ptr2
            
        ptr1 += 1
        ptr2 -= 1

# Test cases
colors = [1, 1, 1, 6, 1, 1, 1]
print(maxDistance(colors))

colors = [1, 8, 3, 8, 3]
print(maxDistance(colors))

colors = [0, 1]
print(maxDistance(colors))

colors = [4,4,4,11,4,4,11,4,4,4,4,4]
print(maxDistance(colors))

colors = [6,6,6,6,6,6,6,6,6,19,19,6,6]
print(maxDistance(colors))

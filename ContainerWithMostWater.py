# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

def maxArea(height):
    ptr1 = 0
    ptr2 = len(height) - 1
    smallest = min(height[ptr1], height[ptr2])
    maxHeight = smallest * (ptr2 - ptr1)

    while ptr1 < ptr2:
        if height[ptr1] < height[ptr2]:
            ptr1 += 1
        else:
            ptr2 -= 1

        smallest = min(height[ptr1], height[ptr2])
        tempHeight = smallest * (ptr2 - ptr1)
        if tempHeight > maxHeight:
            maxHeight = tempHeight

    return maxHeight

#Test cases
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

height = [1,1]
print(maxArea(height))

height = [1,2,1]
print(maxArea(height))

height = [2,3,4,5,18,17,6]
print(maxArea(height))

height = [1,3,2,5,25,24,5]
print(maxArea(height))

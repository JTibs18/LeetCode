# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

def findDiagonalOrder(nums):
    coord = []
    output = []

    for indxY, valY in enumerate(nums):
        for indxX, valX in enumerate(valY): 
            coord.append((indxX + indxY, indxX, valX))

    coord.sort()

    for _, _, val in coord:
        output.append(val)
    
    return output

# Test cases
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findDiagonalOrder(nums))

nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
print(findDiagonalOrder(nums))

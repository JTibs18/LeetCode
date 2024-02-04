# You are given a 0-indexed m x n grid image which represents a grayscale image, where image[i][j] represents a pixel with intensity in the range[0..255]. You are also given a non-negative integer threshold.
# Two pixels image[a][b] and image[c][d] are said to be adjacent if |a - c| + |b - d| == 1.
# A region is a 3 x 3 subgrid where the absolute difference in intensity between any two adjacent pixels is less than or equal to threshold.
# All pixels in a region belong to that region, note that a pixel can belong to multiple regions.
# You need to calculate a 0-indexed m x n grid result, where result[i][j] is the average intensity of the region to which image[i][j] belongs, rounded down to the nearest integer. If image[i][j] belongs to multiple regions, result[i][j] is the average of the rounded down average intensities of these regions, rounded down to the nearest integer. If image[i][j] does not belong to any region, result[i][j] is equal to image[i][j].
# Return the grid result.
# For Weekly Contest #383, Question 3 

def resultGrid(image, threshold):
    imageCoords = dict()
    resultGrid = image 
    row = 0
    col = 0 

    while row + 2 < len(image):
        runningSum = 0 
        isRegion = True

        for i in range(3):
            if abs(image[row + i][col] - image[row + i][col + 1]) > threshold or abs(image[row + i][col + 1] - image[row + i][col + 2]) > threshold:
                isRegion = False  
                break
            else:
                runningSum += sum(image[row + i][col: col + 3])

        for i in range(3):
            if abs(image[row][col + i] - image[row + 1][col + i]) > threshold or abs(image[row + 1][col + i] - image[row + 2][col + i]) > threshold:
                isRegion = False  
                break
        
        if isRegion:
            runningSum = runningSum // 9 

            for i in range(3):
                for j in range(3):
                    if (row + i, col + j) in imageCoords:
                        imageCoords[(row + i, col + j)].append(runningSum)
                    else:
                        imageCoords[(row + i, col + j)] = [runningSum]

        col += 1 

        if col + 2 == len(image[0]):
            col = 0 
            row += 1

    for i in range(len(image)):
        for j in range(len(image[0])):
            if (i, j) in imageCoords:
                resultGrid[i][j] = sum(imageCoords[(i, j)]) // len(imageCoords[(i, j)])

    return resultGrid

# Test cases
image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]]
threshold = 3
print(resultGrid(image, threshold))

image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]]
threshold = 12
print(resultGrid(image, threshold))

image = [[5,6,7],[8,9,10],[11,12,13]]
threshold = 1
print(resultGrid(image, threshold))
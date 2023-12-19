# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

def imageSmoother(img):
    newImage = []

    for indxY, row in enumerate(img):
        newRow = []
        for indxX, val in enumerate(row):
            runningSum = val 
            divisor = 1

            if indxY - 1 >= 0:
                runningSum += img[indxY - 1][indxX] 
                divisor += 1 

                if indxX - 1 >= 0:
                    runningSum += img[indxY - 1][indxX - 1]
                    divisor += 1
                
                if indxX + 1 < len(row):
                    runningSum += img[indxY - 1][indxX + 1]
                    divisor += 1 

            if indxY + 1 < len(img):
                runningSum += img[indxY + 1][indxX]
                divisor += 1

                if indxX - 1 >= 0:
                    runningSum += img[indxY + 1][indxX - 1]
                    divisor += 1
                
                if indxX + 1 < len(row):
                    runningSum += img[indxY + 1][indxX + 1]
                    divisor += 1 

            if indxX - 1 >= 0: 
                runningSum += row[indxX - 1] 
                divisor += 1

            if indxX + 1 < len(row):
                runningSum += row[indxX + 1]
                divisor += 1 
            
            newRow.append(runningSum // divisor)
        
        newImage.append(newRow)
    
    return newImage

# Test cases
img = [[1,1,1],[1,0,1],[1,1,1]]
print(imageSmoother(img))

img = [[100,200,100],[200,50,200],[100,200,100]]
print(imageSmoother(img))
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].

def flipAnImage(image):

    for indx, val in enumerate(image):
        p1 = 0
        p2 = len(image[indx]) - 1

        while (p1 < p2):
            temp = image[indx][p1]
            image[indx][p1] = image[indx][p2]
            image[indx][p2] = temp
            p1 += 1
            p2 -= 1

        for j, num in enumerate(image[indx]):
            if num == 0:
                image[indx][j] = 1
            else:
                image[indx][j] = 0
    return image

#Test Cases
image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAnImage(image))

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAnImage(image))

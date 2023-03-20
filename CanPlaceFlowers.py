# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

def canPlaceFlowers(flowerbed, n):
    if len(flowerbed) == 1 and flowerbed[0] == 0: 
        return n - 1 <= 0 

    for indx, val in enumerate(flowerbed): 
        if val == 0: 
            if (indx - 1 > 0 and flowerbed[indx - 1] == 0) and (indx + 1 < len(flowerbed) and flowerbed[indx + 1] == 0): 
                flowerbed[indx] = 1 
                n -= 1 
            elif indx == 0 and flowerbed[indx + 1] == 0: 
                flowerbed[indx] = 1
                n -= 1 
            elif indx == len(flowerbed) - 1 and flowerbed[indx - 1] == 0: 
                flowerbed[indx] = 1 
                n -= 1 

    return n <= 0

# Test cases
flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))

flowerbed = [1,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))

flowerbed = [0]
n = 1
print(canPlaceFlowers(flowerbed, n))

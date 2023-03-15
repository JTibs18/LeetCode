# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
# Jumbo Burger: 4 tomato slices and 1 cheese slice.
# Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

def numOfBurgers(tomatoSlices, cheeseSlices):
    if tomatoSlices % 2 != 0 or cheeseSlices > tomatoSlices: 
        return []
    
    small = (4 * cheeseSlices - tomatoSlices) // 2
    jumbo = cheeseSlices - small 
    
    if small < 0 or jumbo < 0: 
        return []
    
    return [jumbo, small]

# Test cases
tomatoSlices = 16
cheeseSlices = 7 
print(numOfBurgers(tomatoSlices, cheeseSlices))

tomatoSlices = 17
cheeseSlices = 4
print(numOfBurgers(tomatoSlices, cheeseSlices))

tomatoSlices = 4
cheeseSlices = 17
print(numOfBurgers(tomatoSlices, cheeseSlices))

tomatoSlices = 0 
cheeseSlices = 0 
print(numOfBurgers(tomatoSlices, cheeseSlices))

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

def candy(ratings):
    candies = [1 for i in range(len(ratings))]

    for indx, val in enumerate(ratings): 
        if indx - 1 >= 0 and ratings[indx - 1] < val: 
            candies[indx] = candies[indx - 1] + 1 

    for indx, val in reversed(list(enumerate(ratings))): 
        if indx + 1 < len(ratings) and ratings[indx + 1] < val and candies[indx] <= candies[indx + 1]: 
            candies[indx] = candies[indx + 1] + 1
    
    return sum(candies)

# Test cases
ratings = [1, 0, 2]
print(candy(ratings))

ratings = [1, 2, 2]
print(candy(ratings))

ratings = [1,3,2,2,1]
print(candy(ratings))

ratings = [1,2,87,87,87,2,1]
print(candy(ratings))

ratings = [1,3,4,5,2]
print(candy(ratings))

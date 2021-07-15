# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

def kidsWithCandies(candies, extraCandies):
    mostCandies = max(candies)
    greatest = []

    for kid in candies:
        if (kid + extraCandies) >= mostCandies:
            greatest.append(True)
        else:
            greatest.append(False)
    return greatest

#Test Cases
candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))

candies = [4, 2, 1, 1, 2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))

candies = [12, 1, 12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))

# Design a food rating system that can do the following:
#   Modify the rating of a food item listed in the system.
#   Return the highest-rated food item for a type of cuisine in the system.
# Implement the FoodRatings class:
#   FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
#   foods[i] is the name of the ith food,
#   cuisines[i] is the type of cuisine of the ith food, and
#   ratings[i] is the initial rating of the ith food.
# void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
# String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

# First Attempt: TLE
class FoodRatingsV1:

    def __init__(self, foods, cuisines, ratings):
        self.foodRatings = dict()
        self.cuisinesFood = dict()

        for indx, val in enumerate(foods): 
            self.foodRatings[val] = ratings[indx]
            
            if cuisines[indx] in self.cuisinesFood:
                self.cuisinesFood[cuisines[indx]].append(val)
            else:
                self.cuisinesFood[cuisines[indx]] = [val]
        
    def changeRating(self, food, newRating):
        self.foodRatings[food] = newRating

    def highestRated(self, cuisine):
        maxValue = 0
        foodItem = ''
        for food in self.cuisinesFood[cuisine]:
            if self.foodRatings[food] > maxValue or (self.foodRatings[food] == maxValue and foodItem > food):
                maxValue = self.foodRatings[food]
                foodItem = food 

        return foodItem        

# Second Attempt: runs successfully
from sortedcontainers import SortedSet
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.foodRatings = dict()
        self.foodCuisine = dict()
        self.cuisinesFood = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))

        for indx, val in enumerate(foods): 
            self.foodRatings[val] = ratings[indx]
            self.foodCuisine[val] = cuisines[indx]
            self.cuisinesFood[cuisines[indx]].add((ratings[indx], val))
        
    def changeRating(self, food, newRating):
        oldRating = self.foodRatings[food]
        self.foodRatings[food] = newRating

        self.cuisinesFood[self.foodCuisine[food]].discard((oldRating, food))
        self.cuisinesFood[self.foodCuisine[food]].add((newRating, food))

    def highestRated(self, cuisine):
        return self.cuisinesFood[cuisine][0][1]    

# Test cases
foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

foodRatings = FoodRatings(foods, cuisines, ratings)
print(foodRatings.highestRated("korean"))
print(foodRatings.highestRated("japanese"))
foodRatings.changeRating("sushi", 16)
print(foodRatings.highestRated("japanese"))
foodRatings.changeRating("ramen", 16)
print(foodRatings.highestRated("japanese"))


foods = ['biihw']
cuisines = ['okxsrcqnb']
ratings = [13]

foodRatings = FoodRatings(foods, cuisines, ratings)
foodRatings.changeRating("biihw", 9)
foodRatings.changeRating("biihw", 6)

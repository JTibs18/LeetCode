# You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.
# Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.
# The system should support the following functions:
#   Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
#   Rent: Rents an unrented copy of a given movie from a given shop.
#   Drop: Drops off a previously rented copy of a given movie at a given shop.
#   Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
# Implement the MovieRentingSystem class:
#   MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
#   List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
#   void rent(int shop, int movie) Rents the given movie from the given shop.
#   void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
#   List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
# Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.

# first attempt with Time Limit Exceeded
class MovieRentingSystemV1:

    def __init__(self, n: int, entries):
        self.movies = sorted(entries, key=lambda l:(l[2], l[0], l[1])) 
        self.rentedMovies = []

    def search(self, movie: int):
        cheapestMovies = []

        self.movies = sorted(self.movies, key=lambda l:(l[2], l[0], l[1])) 
        for i in self.movies:
            if i[1] == movie:
                cheapestMovies.append(i[0])

        return cheapestMovies[:5]

    def rent(self, shop: int, movie: int):
        for i in self.movies:
            if i[0] == shop and i[1] == movie:
                self.movies.remove(i)
                self.rentedMovies.append(i)
                break 

    def drop(self, shop: int, movie: int):
        for i in self.rentedMovies:
            if i[0] == shop and i[1] == movie:
                self.rentedMovies.remove(i)
                self.movies.append(i)
                break 

    def report(self):
        self.rentedMovies = sorted(self.rentedMovies, key=lambda l:(l[2], l[0], l[1]))
        cheapestMovies = []

        for i in range(0, min(5, len(self.rentedMovies))):
            cheapestMovies.append([self.rentedMovies[i][0], self.rentedMovies[i][1]])

        return cheapestMovies 
    
# second attempt, with help from https://leetcode.com/problems/design-movie-rental-system/solutions/3852718/python/?envType=list&envId=5bfcfj7j
from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries):
        self.movies = defaultdict(SortedList)
        self.shop = dict()

        for s, m, p in entries: 
            self.shop[(s, m)] = p
            self.movies[m].add((p, s))

        self.rentedMovies = SortedList()

    def search(self, movie: int):
        if movie in self.movies: 
            return [v for _, v in self.movies[movie][:5]]
        return []

    def rent(self, shop: int, movie: int):
        price = self.shop[(shop, movie)]
        self.movies[movie].remove((price, shop))
        self.rentedMovies.add((price, shop, movie))

    def drop(self, shop: int, movie: int):
        price = self.shop[(shop, movie)]
        self.movies[movie].add((price, shop))
        self.rentedMovies.remove((price, shop, movie))

    def report(self):
        return [[s, m] for _, s, m in self.rentedMovies[:5]]

# Test cases
n = 3
entries = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
obj = MovieRentingSystem(n, entries)
print(obj.search(1))
obj.rent(0, 1)
obj.rent(1, 2)
print(obj.report())
obj.drop(1, 2)
print(obj.search(2))

["MovieRentingSystem","rent","report","rent","report","rent","report","rent","rent","rent","report"]
[[1,[[0,1,3],[0,5,3],[0,7,3],[0,6,3],[0,2,3],[0,3,3],[0,4,3],[0,8,3]]],[0,1],[],[0,4],[],[0,3],[],[0,2],[0,6],[0,7], []]

n = 1 
entries = [[0,1,3],[0,5,3],[0,7,3],[0,6,3],[0,2,3],[0,3,3],[0,4,3],[0,8,3]]
obj2 = MovieRentingSystem(n, entries)
obj2.rent(0, 1)
print(obj2.report())
obj2.rent(0, 4)
print(obj2.report())
obj2.rent(0, 3)
print(obj2.report())
obj2.rent(0, 2)
obj2.rent(0, 6)
obj2.rent(0, 7)
print(obj2.report())
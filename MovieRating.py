# Write a solution to:
#   Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
#   Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

import pandas as pd

def movieRating(movies, users, movie_rating):
    mergeTable = pd.merge(movies, movie_rating, on='movie_id').merge(users, on='user_id')
    userMostRatedMoviesMergedTable = mergeTable.copy()
    movieWithHighestRatingTable = mergeTable.copy()
    
    userMostRatedMoviesMergedTable['count'] = userMostRatedMoviesMergedTable.groupby('user_id')['user_id'].transform('count')
    userMostRatedMovies = userMostRatedMoviesMergedTable[['user_id', 'count', 'name']].drop_duplicates().reset_index().sort_values(by=['count', 'name'], ascending=[False, True]).iloc[0]['name']

    movieWithHighestRatingTable['average'] = movieWithHighestRatingTable[(movieWithHighestRatingTable['created_at'] >= "2020-02-01") & (movieWithHighestRatingTable['created_at'] <= "2020-02-29")].groupby('title')['rating'].transform('mean')
    movieWithHighestRated = movieWithHighestRatingTable[['average', 'title']].drop_duplicates().reset_index().sort_values(by=['average', 'title'], ascending=[False, True]).iloc[0]['title']

    return pd.DataFrame(data=[userMostRatedMovies, movieWithHighestRated], columns=['results'])

# Test cases
data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id':'Int64', 'title':'object'})
data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'], [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'], [3, 2, 4, '2020-02-25']]
movie_rating = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype({'movie_id':'Int64', 'user_id':'Int64', 'rating':'Int64', 'created_at':'datetime64[ns]'})
print(movieRating(movies, users, movie_rating))
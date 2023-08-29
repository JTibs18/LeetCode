# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
# Return the result table in any order.

import pandas as pd 

def actors_and_directors(actor_director): 
    actorDirectorCount = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    return actorDirectorCount[actorDirectorCount['timestamp'] >= 3][['actor_id', 'director_id']]

# schema
data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
ActorDirector = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})
print(actors_and_directors(ActorDirector))
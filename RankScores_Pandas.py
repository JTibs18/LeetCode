# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
#   The scores should be ranked from the highest to the lowest.
#   If there is a tie between two scores, both should have the same ranking.
#   After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

import pandas as pd

def order_scores(scores):
    scores['rank'] = scores.score.rank(method='dense', ascending=False)
    return scores.sort_values(by='rank')[['score', 'rank']]

# schema 
data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
Scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
print(order_scores(Scores))
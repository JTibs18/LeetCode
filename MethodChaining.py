# Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
# Return the animals sorted by weight in descending order.

import pandas as pd

def findHeavyAnimals(animals):
    return animals[animals['weight'] > 100].sort_values(by=['weight'], ascending=False)[['name']]

# Test cases
data = [['Tatiana', 'Snake', 98, 464],
        ['Khaled', 'Giraffe', 50, 41],
        ['Alex', 'Leopard', 6, 328],
        ['Jonathan', 'Monkey', 45, 463],
        ['Stefan', 'Bear', 100, 50],
        ['Tommy', 'Panda', 26, 349]]
animals = pd.DataFrame(data, columns=['name', 'species', 'age', 'weight'])
print(findHeavyAnimals(animals))
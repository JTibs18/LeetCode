# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

def destCity(paths):
    outgoingCities = set()
    incomingCities = set()

    for i in paths: 
        outgoingCities.add(i[0])
        incomingCities.add(i[1])

    return (incomingCities - outgoingCities).pop() 

# Test cases
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(destCity(paths))

paths = [["A","Z"]]
print(destCity(paths))

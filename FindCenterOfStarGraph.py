# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

def findCenter(edges):
    graph = dict()

    for nodeA, nodeB in edges:
        if nodeA in graph:
            graph[nodeA] += 1
        else:
            graph[nodeA] = 1
        
        if nodeB in graph:
            graph[nodeB] += 1
        else:
            graph[nodeB] = 1

    for key, val in graph.items():
        if val == len(graph) - 1:
            return key

# Test cases
edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))

edges = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges))

edges = [[1, 3], [2, 3]]
print(findCenter(edges))

# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.
# Implement the Graph class:
#   Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
#   addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
#   int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
# with Dijkstra algorithm help from https://www.youtube.com/watch?v=isMmhv1eB_U

import heapq

class Graph:

    def __init__(self, n, edges):
        self.graph = dict()
        self.size = n 

        for fromNode, toNode, weight in edges: 
            if fromNode in self.graph: 
                self.graph[fromNode].append((toNode, weight))
            else:
                self.graph[fromNode] = [(toNode, weight)]
            

    def addEdge(self, edge):
        fromNode, toNode, weight = edge 
        self.size += 1    

        if fromNode in self.graph:
            self.graph[fromNode].append((toNode, weight))
        else:
            self.graph[fromNode] = [(toNode, weight)]    


    def shortestPath(self, node1, node2):
        distanceToNodes = {node: float('inf') for node in range(0, self.size)} 
        queueToVisit = []
        
        distanceToNodes[node1] = 0 
        heapq.heappush(queueToVisit, (0, node1))

        while queueToVisit: 
            currentWeight, currentNode = heapq.heappop(queueToVisit)

            if distanceToNodes[currentNode] < currentWeight or currentNode not in self.graph:
                continue 
            
            for nextNode, weight in self.graph[currentNode]:
                newWeight = currentWeight + weight

                if newWeight < distanceToNodes[nextNode]:
                    distanceToNodes[nextNode] = newWeight
                    heapq.heappush(queueToVisit, (newWeight, nextNode))

        if distanceToNodes[node2] == float('inf'):
            return -1 
        return distanceToNodes[node2]

# Test cases
n = 4 
edges = [[0, 2, 5],
         [0, 1, 2],
         [1, 2, 1],
         [3, 0, 3]]
graph = Graph(n, edges)
print(graph.shortestPath(3, 2))
print(graph.shortestPath(0, 3))
graph.addEdge([1, 3, 4])
print(graph.shortestPath(0, 3))

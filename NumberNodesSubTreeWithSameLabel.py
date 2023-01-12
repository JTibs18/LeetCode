# You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).
# The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.
# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.
# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

# Completed with help from https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/3038104/python3-dfs-explained/
from collections import Counter

def countSubTrees(n, edges, labels): 
    answer = [0 for i in range(n)]
    connections = dict()

    for i in edges: 
        if i[0] in connections: 
            connections[i[0]].append(i[1])
        else: 
            connections[i[0]] = [i[1]]

        if i[1] in connections: 
            connections[i[1]].append(i[0])
        else: 
            connections[i[1]] = [i[0]]

    def dfs(cur, parent): 
        nonlocal answer 
        count = Counter()

        for i in connections[cur]: 
            if i != parent: 
                count += dfs(i, cur)

        count[labels[cur]] += 1 
        answer[cur] = count[labels[cur]]
        return count 

    dfs(0, -1)
    return answer
        
# Test cases
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
print(countSubTrees(n, edges, labels))

n = 4
edges = [[0,1],[1,2],[0,3]]
labels = "bbbb"
print(countSubTrees(n, edges, labels))

n = 5
edges = [[0,1],[0,2],[1,3],[0,4]]
labels = "aabab"
print(countSubTrees(n, edges, labels))

n = 4
edges = [[0,2], [0,3], [1,2]]
labels = "aeed"
print(countSubTrees(n, edges, labels))

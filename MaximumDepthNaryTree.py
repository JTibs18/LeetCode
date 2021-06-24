# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root):
    if root == None:
        return 0
    elif root.children == None or len(root.children) == 0:
        return 1
    else:
        return max(maxDepth(c) for c in root.children) + 1

#Test cases
root = Node(1)
node1 = Node(3)
node2 = Node(2)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
root.children = [node1, node2, node3]
node1.children = [node4, node5]
print(maxDepth(root))

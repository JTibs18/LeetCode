# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def levelOrder(root):
    levels = dict()

    if not root:
        return []

    queue = [(root, 0)]

    while queue:
        curNode, curLev = queue.pop(0)

        if curLev in levels:
            levels[curLev].append(curNode.val)
        else:
            levels[curLev] = [curNode.val]

        if curNode.children:
            for i in curNode.children:
                queue.append((i, curLev + 1))

    return list(levels.values())

# Test cases
root = Node(1)
n1 = Node(3)
n2 = Node(2)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
root.children = [n1, n2, n3]
n1.children = [n4, n5]
print(levelOrder(root))

root = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
n6 = Node(7)
n7 = Node(8) 
n8 = Node(9)
n9 = Node(10)
n10 = Node(11)
n11 = Node(12)
n12 = Node(13)
n13 = Node(14)
root.children = [n1, n2, n3, n4]
n2.children = [n5, n6]
n3.children = [n7]
n4.children = [n8, n9]
n6.children = [n10]
n7.children = [n11]
n8.children = [n12]
n10.children = [n13]
print(levelOrder(root))

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    levels = dict()
    queue = [(root, 0)]

    if not root:
        return 

    while queue:
        curNode, level = queue.pop(0)

        if level in levels:
            levels[level].append(curNode)
        else:
            levels[level] = [curNode]

        if curNode.left:
            queue.append((curNode.left, level + 1))

        if curNode.right:
            queue.append((curNode.right, level + 1))

        
    for nodes in levels.values():
        for indx in range(len(nodes) - 1):
            nodes[indx].next = nodes[indx + 1]

    return root

# Test cases
root = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
n6 = Node(7)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
print(connect(root))

print(connect(None))
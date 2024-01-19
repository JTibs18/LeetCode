# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    levels = dict()
    queue = [(root, 0)]
    traversal = []

    if not root:
        return traversal

    while queue:
        curNode, level = queue.pop(0)

        if level in levels:
            levels[level].append(curNode.val)
        else:
            levels[level] = [curNode.val]

        if curNode.left:
            queue.append((curNode.left, level + 1))
        
        if curNode.right:
            queue.append((curNode.right, level + 1))

    for val in levels.values():
        traversal.append(val)

    return traversal[::-1]

# Test cases
root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
print(levelOrderBottom(root))

root = TreeNode(1)
print(levelOrderBottom(root))

print(levelOrderBottom(None))
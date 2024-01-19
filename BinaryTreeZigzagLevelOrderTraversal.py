# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    levels = dict()
    queue = [(root, 0)]
    zigZag = []

    if root == None:
        return zigZag

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
    
    for key, val in levels.items():
        if key % 2 != 0:
            val = val[::-1]
        zigZag.append(val)

    return zigZag

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
print(zigzagLevelOrder(root))

root = TreeNode(1)
print(zigzagLevelOrder(root))

print(zigzagLevelOrder(None))

root = TreeNode(0)
n1 = TreeNode(2)
n2 = TreeNode(4)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(-1)
n6 = TreeNode(5)
n7 = TreeNode(1)
n8 = TreeNode(6)
n9 = TreeNode(8)
root.left = n1
root.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.right = n8
n5.right = n9
print(zigzagLevelOrder(root))

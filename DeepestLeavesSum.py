# Given the root of a binary tree, return the sum of values of its deepest leaves.
 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root):
    queue = [(root, 1)]
    maxLevel = 1
    leafValues = []

    while queue:
        curNode, level = queue.pop(0)

        if curNode.right:
            queue.append((curNode.right, level + 1))
            maxLevel = max(level + 1, maxLevel)

        if curNode.left:
            queue.append((curNode.left, level + 1))
            maxLevel = max(level + 1, maxLevel)

        if not curNode.left and not curNode.right:
            leafValues.append((curNode.val, level))

    return sum([x[0] for x in leafValues if x[1] == maxLevel])

# Test cases
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)
n6 = TreeNode(7)
n7 = TreeNode(8)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
n3.left = n6
n5.right = n7
print(deepestLeavesSum(root))

root = TreeNode(6)
n1 = TreeNode(7)
n2 = TreeNode(8)
n3 = TreeNode(2)
n4 = TreeNode(7)
n5 = TreeNode(1)
n6 = TreeNode(3)
n7 = TreeNode(9)
n8 = TreeNode(1)
n9 = TreeNode(4)
n10 = TreeNode(5)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n3.left = n7
n4.right = n8
n4.left = n9 
n6.right = n10
print(deepestLeavesSum(root))

root = TreeNode(38)
n1 = TreeNode(43)
n2 = TreeNode(70)
n3 = TreeNode(16)
n4 = TreeNode(78)
n5 = TreeNode(91)
n6 = TreeNode(71)
n7 = TreeNode(27)
n8 = TreeNode(71)
n9 = TreeNode(71)
root.left = n1
root.right = n2
n1.left = n3
n2.left = n4
n2.right = n5 
n3.right = n6
n4.left = n7
n5.left = n8
n7.left = n9
print(deepestLeavesSum(root))

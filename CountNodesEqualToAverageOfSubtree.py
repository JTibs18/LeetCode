# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
# Note:
# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfSubtree(root):

    def helper(curNode):
        if not curNode.left and not curNode.right:
            return (curNode.val, 1, 1)
        
        total = 0
        avg = curNode.val
        nodeCount = 1
        
        if curNode.left:
            curAvg, curNumNodes, numEqual = helper(curNode.left)
            total += numEqual
            avg += curAvg
            nodeCount += curNumNodes

        if curNode.right:
            curAvg, curNumNodes, numEqual = helper(curNode.right)
            total += numEqual
            avg += curAvg
            nodeCount += curNumNodes
        
        if avg // nodeCount == curNode.val:
            total += 1 
        
        return (avg, nodeCount, total)

    return helper(root)[2]

# Test cases
root = TreeNode(4)
n1 = TreeNode(8)
n2 = TreeNode(5)
n3 = TreeNode(0)
n4 = TreeNode(1)
n5 = TreeNode(6)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
print(averageOfSubtree(root))

root = TreeNode(1)
print(averageOfSubtree(root))
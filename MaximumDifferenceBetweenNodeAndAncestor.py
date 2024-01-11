# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(root):
    def helper(curNode, maxAncestor, minAncestor, maxDiff):
        if curNode != root:
            maxDiff = max(maxDiff, abs(maxAncestor - curNode.val), abs(minAncestor - curNode.val))

        maxAncestor = max(maxAncestor, curNode.val)
        minAncestor = min(minAncestor, curNode.val)

        if curNode.left and curNode.right:
            return max(helper(curNode.left, maxAncestor, minAncestor, maxDiff), helper(curNode.right, maxAncestor, minAncestor, maxDiff))

        if curNode.left:
            return helper(curNode.left, maxAncestor, minAncestor, maxDiff)

        if curNode.right:
            return helper(curNode.right, maxAncestor, minAncestor, maxDiff)
        
        return maxDiff
    
    return helper(root, 0, root.val, 0)
         
# Test cases
root = TreeNode(8)
n1 = TreeNode(3)
n2 = TreeNode(10)
n3 = TreeNode(1)
n4 = TreeNode(6)
n5 = TreeNode(14)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(13)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
n4.left = n6
n4.right = n7
n5.left = n8
print(maxAncestorDiff(root))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(0)
n3 = TreeNode(3)
root.right = n1
n1.right = n2
n2.left = n3
print(maxAncestorDiff(root))

# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.
# A grandparent of a node is the parent of its parent if it exists.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root):

    def helper(grandparentVal, parentVal, curNode):
        if grandparentVal % 2 == 0 and grandparentVal != -1:
            curVal = curNode.val
        else:
            curVal = 0

        if curNode.left and curNode.right:
            return helper(parentVal, curNode.val, curNode.left) + helper(parentVal, curNode.val, curNode.right) + curVal

        if curNode.left:
            return helper(parentVal, curNode.val, curNode.left) + curVal
        
        if curNode.right:
            return helper(parentVal, curNode.val, curNode.right) + curVal
        
        return curVal

    if root.left and root.right:
        return helper(-1, root.val, root.left) + helper(-1, root.val, root.right)

    if root.left:
        return helper(-1, root.val, root.left)
    
    if root.right:
        return helper(-1, root.val, root.right)
    
    return 0 

# Test cases
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
n4.left = n8
n4.right = n9
n6.right = n10
print(sumEvenGrandparent(root))

root = TreeNode(1)
print(sumEvenGrandparent(root))

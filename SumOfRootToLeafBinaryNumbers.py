# You are given the root of a binary tree where each node has a value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root):
    total = 0 

    def helperFun(curNode, total, curBinary):
        newBinary = curBinary + str(curNode.val)

        if not curNode.left and not curNode.right:
            return int(newBinary, 2) + total 
        
        if curNode.left and curNode.right:
            return helperFun(curNode.left, total, newBinary) + helperFun(curNode.right, total, newBinary)
        elif curNode.left:
            return helperFun(curNode.left, total, newBinary)
        elif curNode.right:
            return helperFun(curNode.right, total, newBinary)

    return helperFun(root, total, "")    

#Test Cases
r = TreeNode(1)
node1 = TreeNode(0)
node2 = TreeNode(1)
node3 = TreeNode(0)
node4 = TreeNode(1)
node5 = TreeNode(0)
node6 = TreeNode(1)
r.left = node1
r.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
print(sumRootToLeaf(r))

r = TreeNode(0)
print(sumRootToLeaf(r))

r = TreeNode(1)
node1 = TreeNode(1)
r.left = node1
print(sumRootToLeaf(r))
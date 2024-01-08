# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.
# Return a reference to the same node in the cloned tree.
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getTargetCopy(original, cloned, target):
    def helperFun(curNode, clonedNode):
        if curNode == target:
            return clonedNode
        
        if curNode.right and curNode.left:
            return helperFun(curNode.right, clonedNode.right) or helperFun(curNode.left, clonedNode.left)
        elif curNode.left:
            return helperFun(curNode.left, clonedNode.left)
        elif curNode.right:
            return helperFun(curNode.right, clonedNode.right)

    return helperFun(original, cloned)

# Test cases
root = TreeNode(7)
n1 = TreeNode(4)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(19)
root.left = n1
root.right = n2
n2.left = n3
n3.right = n4 
target = n2
print(getTargetCopy(root, root, target))

root = TreeNode(7)
target = root
print(getTargetCopy(root, root, target))

root = TreeNode(8)
n1 = TreeNode(6)
n2 = TreeNode(5)
n3 = TreeNode(4)
n4 = TreeNode(3)
n5 = TreeNode(2)
n6 = TreeNode(1)
root.right = n1
n1.right = n2
n2.right = n3
n3.right = n4
n4.right = n5
n5.right = n6
target = n3
print(getTargetCopy(root, root, target))

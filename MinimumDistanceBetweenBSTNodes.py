# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root):
    indx = 0 
    diff = 10000000
    foundNodes = []

    def inOrderTraversal(root, foundNodes): 
        if root.left: 
            inOrderTraversal(root.left, foundNodes)

        foundNodes.append(root.val)

        if root.right: 
            inOrderTraversal(root.right, foundNodes)

    inOrderTraversal(root, foundNodes)

    while indx < len(foundNodes) - 1: 
        if foundNodes[indx + 1] - foundNodes[indx] < diff: 
            diff = foundNodes[indx + 1] - foundNodes[indx]
        indx += 1
    
    return diff

# Test cases
root = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(6)
node3 = TreeNode(1)
node4 = TreeNode(3)
root.left = node1
root.right = node2
node1.left = node3 
node1.right = node4
print(minDiffInBST(root))

root = TreeNode(1)
node1 = TreeNode(0)
node2 = TreeNode(48)
node3 = TreeNode(12)
node4 = TreeNode(49)
root.left = node1 
root.right = node2
node2.left = node3
node2.right = node4 
print(minDiffInBST(root))

root = TreeNode(71)
node1 = TreeNode(62)
node2 = TreeNode(84)
node3 = TreeNode(14)
node4 = TreeNode(88)
root.left = node1 
root.right = node2
node1.left = node3
node2.right = node4
print(minDiffInBST(root))


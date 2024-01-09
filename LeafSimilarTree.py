# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1, root2):

    def helper(curNode, leaves):
        if not curNode.left and not curNode.right:
            leaves.append(curNode.val)
            return leaves

        if curNode.left:
            helper(curNode.left, leaves)
        
        if curNode.right:
            helper(curNode.right, leaves)

        return leaves 
    
    leaf1 = helper(root1, [])
    leaf2 = helper(root2, [])

    if len(leaf1) != len(leaf2):
        return False 

    for i in range(len(leaf1)):
        if leaf1[i] != leaf2[i]:
            return False
        
    return True 

# Test cases
root1 = TreeNode(3)
n1 = TreeNode(5)
n2 = TreeNode(1)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(9)
n6 = TreeNode(8)
n7 = TreeNode(7)
n8 = TreeNode(4)
root1.left = n1
root1.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n4.left = n7
n4.right = n8

root2 = TreeNode(3)
r2n1 = TreeNode(5)
r2n2 = TreeNode(1)
r2n3 = TreeNode(6)
r2n4 = TreeNode(7)
r2n5 = TreeNode(4)
r2n6 = TreeNode(2)
r2n7 = TreeNode(9)
r2n8 = TreeNode(8)
root2.left = r2n1
root2.right = r2n2
r2n1.left = r2n3
r2n1.right = r2n4
r2n2.left = r2n5
r2n2.right = r2n6
r2n6.left = r2n7
r2n6.right = r2n8

print(leafSimilar(root1, root2))

root1 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root1.left = n1
root2.right = n2

root2 = TreeNode(1)
r2n2 = TreeNode(3)
r2n3 = TreeNode(2)
root2.left = r2n2
root2.right = r2n3

print(leafSimilar(root1, root2))

root1 = TreeNode(1)
root2 = TreeNode(1)
print(leafSimilar(root1, root2))
#Given the root of a binary tree, return the sum of all left leaves.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if root == None:
        return 0
    elif root.left != None and root.left.left == None and root.left.right == None:
        return root.left.val + sumOfLeftLeaves(root.right)
    else:
        return sumOfLeftLeaves(root.right) + sumOfLeftLeaves(root.left)

#Test Case
r = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
r.left = node1
r.right = node2
node2.left = node3
node2.right = node4
print(sumOfLeftLeaves(r))

r = TreeNode(1)
print(sumOfLeftLeaves(r))

r = TreeNode(1)
node1 = TreeNode(2)
r.right = node1
print(sumOfLeftLeaves(r))

r1 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
r1.left = node1
r1.right = node2
node1.left = node3
node1.right = node4
print(sumOfLeftLeaves(r1))

r2 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
r2.left = node1
node1.left = node2
node2.left = node3
node3.left = node4
print(sumOfLeftLeaves(r2))

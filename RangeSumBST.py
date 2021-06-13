# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):
        if root == None:
            return 0
        elif root.val < low:
            return (rangeSumBST(root.right, low, high))
        elif root.val > high:
            return (rangeSumBST(root.left, low, high))
        else:
            return rangeSumBST(root.right, low, high) + rangeSumBST(root.left, low, high) + root.val 

#Test cases
r1 = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(3)
node3 = TreeNode(7)
node4 = TreeNode(15)
node5 = TreeNode(18)
r1.left = node1
r1.right = node4
node1.left = node2
node1.right = node3
node4.right = node5
print(rangeSumBST(r1, 7, 15))

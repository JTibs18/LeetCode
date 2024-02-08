# A binary tree is named Even-Odd if it meets the following conditions:
#   The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
#   For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
#   For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isEvenOddTree(root):
    levels = dict()
    q = [(root, 0)]

    while q:
        curNode, curLevel = q.pop(0)

        if (curLevel % 2 == 0 and curNode.val % 2 == 0) or (curLevel % 2 != 0 and curNode.val % 2 != 0):
            return False 
        
        if curLevel in levels:
            if (curLevel % 2 == 0 and levels[curLevel][-1] >= curNode.val) or (curLevel % 2 != 0 and levels[curLevel][-1] <= curNode.val):
                return False
            levels[curLevel].append(curNode.val)
        else:
            levels[curLevel] = [curNode.val]

        if curNode.left:
            q.append((curNode.left, curLevel + 1))

        if curNode.right:
            q.append((curNode.right, curLevel + 1))
        
    return True 

# Test cases
root = TreeNode(1)
n1 = TreeNode(10)
n2 = TreeNode(4)
n3 = TreeNode(3)
n4 = TreeNode(7)
n5 = TreeNode(9)
n6 = TreeNode(12)
n7 = TreeNode(8)
n8 = TreeNode(6)
n9 = TreeNode(2)
root.left = n1
root.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n5.right = n9
print(isEvenOddTree(root))

root = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(3)
n5 = TreeNode(7)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5 
print(isEvenOddTree(root))

root = TreeNode(5)
n1 = TreeNode(9)
n2 = TreeNode(1)
n3 = TreeNode(3)
n4 = TreeNode(5)
n5 = TreeNode(7)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5 
print(isEvenOddTree(root))
# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pseudoPalindromicPaths(root):
    def helper(curNode, collectedVals):
        valCount = copy.deepcopy(collectedVals)
        
        if curNode.val not in valCount:
            valCount[curNode.val] = 1 
        else:
            valCount[curNode.val] += 1

        if not curNode.left and not curNode.right:
            oddCount = 0 
        
            for val in valCount.values():
                if val % 2 != 0:
                    oddCount += 1 

            if oddCount <= 1:
                return 1
            return 0

        if curNode.left and curNode.right:
            return helper(curNode.left, valCount) + helper(curNode.right, valCount)
        
        if curNode.left:
            return helper(curNode.left, valCount)
        
        if curNode.right:
            return helper(curNode.right, valCount)

    return helper(root, dict())

# Test cases
root = TreeNode(2)
n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(3)
n4 = TreeNode(1)
n5 = TreeNode(1)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
print(pseudoPalindromicPaths(root))

root = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(1)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n4.right = n5
print(pseudoPalindromicPaths(root))
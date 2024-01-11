# Given a binary tree with the following rules:
#   root.val == 0
#   If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
#   If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
# Implement the FindElements class:
#   FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
#   bool find(int target) Returns true if the target value exists in the recovered binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# slower solution that uses less memory
class FindElements1:
    def __init__(self, root):
        self.newTree = TreeNode(0)

        def helper(originalTree, newTree):
            if originalTree and originalTree.left:
                newTree.left = TreeNode(2 * newTree.val + 1)
                helper(originalTree.left, newTree.left)

            if originalTree and originalTree.right:
                newTree.right = TreeNode(2 * newTree.val + 2)
                helper(originalTree.right, newTree.right)
            
        helper(root, self.newTree)
        
    def find(self, target):
        def helper(curNode):
            if curNode.val == target:
                return True 
            
            if curNode.left and curNode.right:
                return helper(curNode.left) or helper(curNode.right)
            
            if curNode.left:
                return helper(curNode.left)
            
            if curNode.right:
                return helper(curNode.right)
            
            return False 
        
        return helper(self.newTree)

# faster solution, uses more memory
class FindElements:
    def __init__(self, root):
        self.newTree = TreeNode(0)
        self.foundNumbers = [0]

        def helper(originalTree, newTree):
            if originalTree and originalTree.left:
                leftVal = (2 * newTree.val + 1)
                newTree.left = TreeNode(leftVal)
                self.foundNumbers.append(leftVal)
                helper(originalTree.left, newTree.left)

            if originalTree and originalTree.right:
                rightVal = 2 * newTree.val + 2
                newTree.right = TreeNode(rightVal)
                self.foundNumbers.append(rightVal)
                helper(originalTree.right, newTree.right)
            
        helper(root, self.newTree)
        
    def find(self, target):
        return target in self.foundNumbers

# Test cases
root = TreeNode(-1)
n1 = TreeNode(-1)
root.right = n1  
findElements = FindElements(root)
print(findElements.find(1))
print(findElements.find(2))

root = TreeNode(-1)
n1 = TreeNode(-1)
n2 = TreeNode(-1)
n3 = TreeNode(-1)
n4 = TreeNode(-1)
root.left = n1
root.right = n2
n1.left = n3
n2.right = n4
findElements = FindElements(root)
print(findElements.find(1))
print(findElements.find(3))
print(findElements.find(5))

root = TreeNode(-1)
n1 = TreeNode(-1)
n2 = TreeNode(-1)
n3 = TreeNode(-1)
root.right = n1
n1.left = n2
n2.left = n3 
findElements = FindElements(root)
print(findElements.find(2))
print(findElements.find(3))
print(findElements.find(4))
print(findElements.find(5))

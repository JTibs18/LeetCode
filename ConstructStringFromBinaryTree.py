# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root):
    def helperFun(node, curString):
        curString += "(" + str(node.val)
        
        if node.right and not node.left:
            curString += "()"
        elif node.left:
            curString = helperFun(node.left, curString)
            
        if node.right:
            curString = helperFun(node.right, curString)

        return curString + ")"
    
    curString = ''
    
    return helperFun(root, curString)[1:-1]

# Test cases
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
root.right = node2
root.left = node1
node1.left = node3 
print(tree2str(root))

r1 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
r1.right = n2
r1.left = n1
n1.right = n3 
print(tree2str(r1))

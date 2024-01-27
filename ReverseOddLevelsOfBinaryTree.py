# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
#   For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
# The level of a node is the number of edges along the path between it and the root node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOddLevels(root):
    levels = dict()
    q = [(root, 0)]
    allNodes = []

    if not root.left:
        return root
    
    while q:
        curNode, curLev = q.pop(0)

        if curLev % 2 != 0: 
            if curLev in levels:
                levels[curLev].append(curNode.val)
            else:
                levels[curLev] = [curNode.val]

        if curNode.left:
            q.extend([(curNode.left, curLev + 1) , (curNode.right, curLev + 1)])
        
    for values in levels.values():
        allNodes.extend(values[::-1])
    
    q = [root.left, root.right]
    indx = 0

    while q:
        curNode = q.pop(0)
        curNode.val = allNodes[indx]

        if curNode.left and curNode.left.left:
            q.extend([curNode.left.left, curNode.left.right, curNode.right.left, curNode.right.right])
        
        indx += 1

    return root

# Test cases
root = TreeNode(2)
n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(8)
n4 = TreeNode(13)
n5 = TreeNode(21)
n6 = TreeNode(34)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
print(reverseOddLevels(root))

root = TreeNode(7)
n1 = TreeNode(13)
n2 = TreeNode(11)
root.left = n1
root.right = n2
print(reverseOddLevels(root))

root = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(0)
n4 = TreeNode(0)
n5 = TreeNode(0)
n6 = TreeNode(0)
n7 = TreeNode(1)
n8 = TreeNode(1)
n9 = TreeNode(1)
n10 = TreeNode(1)
n11 = TreeNode(2)
n12 = TreeNode(2)
n13 = TreeNode(2)
n14 = TreeNode(2)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n3.left = n7
n3.right = n8
n4.left = n9
n4.right = n10
n5.left = n11
n5.right = n12
n6.left = n13
n6.right = n14
print(reverseOddLevels(root))

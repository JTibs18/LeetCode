# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
# Return the vertical order traversal of the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    verticalCoords = dict()
    q = [(root, 0, 0)]
    verticalTrav = []
    prev = float("inf")

    while q:
        curNode, curX, curY = q.pop(0)

        if (curX, curY) in verticalCoords:
            verticalCoords[(curX, curY)].append(curNode.val)
        else:
            verticalCoords[(curX, curY)] = [curNode.val]

        if curNode.left:
            q.append((curNode.left, curX - 1, curY + 1))
        
        if curNode.right:
            q.append((curNode.right, curX + 1, curY + 1))

    for key, val in sorted(verticalCoords.items()):
        if key[0] == prev:
            verticalTrav[-1].extend(sorted(val))
        else:
            verticalTrav.append(sorted(val))
            prev = key[0]

    return verticalTrav

# Test cases
root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4 
print(verticalTraversal(root))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)
n6 = TreeNode(7)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6 
print(verticalTraversal(root))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(6)
n5 = TreeNode(5)
n6 = TreeNode(7)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6 
print(verticalTraversal(root))
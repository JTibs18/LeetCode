# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same distance from the root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargestLevelSum(root, k):
    sums = []
    queue = [(root, 0)]

    while queue:
        curNode, curLevel = queue.pop()

        if curNode.left:
            queue.append((curNode.left, curLevel + 1))

        if curNode.right:
            queue.append((curNode.right, curLevel + 1))

        if curLevel >= len(sums):
            sums.append(curNode.val)
        else:
            sums[curLevel] += curNode.val

    if len(sums) < k:
        return -1

    sums.sort(reverse=True)
    return sums[k - 1]

# Test cases
root = TreeNode(5)
n1 = TreeNode(8)
n2 = TreeNode(9)
n3 = TreeNode(2)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(7)
n7 = TreeNode(4)
n8 = TreeNode(6)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n3.left = n7
n3.right = n8 
k = 2
print(kthLargestLevelSum(root, k))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.left = n1
n1.left = n2 
k = 1
print(kthLargestLevelSum(root, k))
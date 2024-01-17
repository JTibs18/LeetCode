# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# naive attempt
def levelOrder1(root):
    if not root: 
        return []
    
    order = []
    queue = [(root, 0)]
    curLevel = []
    curLevelNum = 0

    while queue:
        curNode, level = queue.pop(0)

        if level != curLevelNum:
            order.append(curLevel)
            curLevel = []
            curLevelNum += 1

        curLevel.append(curNode.val)

        if curNode.left:
            queue.append((curNode.left, level + 1))

        if curNode.right:
            queue.append((curNode.right, level + 1))

    order.append(curLevel)
    return order

# faster and more space efficient solution
def levelOrder(root):
    if not root: 
        return []
    
    order = []
    queue = [(root, 0)]
    levelDict = dict()

    while queue:
        curNode, level = queue.pop(0)

        if level not in levelDict:
            levelDict[level] = [curNode.val]
        else:
            levelDict[level].append(curNode.val)

        if curNode.left:
            queue.append((curNode.left, level + 1))

        if curNode.right:
            queue.append((curNode.right, level + 1))

    for arr in levelDict.values():
        order.append(arr)

    return order

# Test cases
root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
root.left = n1
root.right = n2
n2.right = n3
n2.left = n4
print(levelOrder(root))

root = TreeNode(1)
print(levelOrder(root))

print(levelOrder(None))
 
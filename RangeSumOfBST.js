// Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

function rangeSumBST(root, low, high){
    total = 0 

    function helper(curNode){
        if (curNode.val >= low && curNode.val <= high){
            total += curNode.val
        }

        if (curNode.left == null && curNode.right == null){
            return 
        }

        if (curNode.left != null){
            helper(curNode.left, total)
        }

        if (curNode.right != null){
            helper(curNode.right, total)
        }
    }

    helper(root, total)
    return total
}

// Test cases
root = new TreeNode(10)
n1 = new TreeNode(5)
n2 = new TreeNode(3)
n3 = new TreeNode(7)
n4 = new TreeNode(15)
n5 = new TreeNode(18)
root.left = n1
root.right = n4
n1.left = n2
n1.right = n3
n4.right = n5 
low = 7
high = 15
console.log(rangeSumBST(root, low, high))

root = new TreeNode(10)
n1 = new TreeNode(5)
n2 = new TreeNode(15)
n3 = new TreeNode(3)
n4 = new TreeNode(7)
n5 = new TreeNode(13)
n6 = new TreeNode(18)
n7 = new TreeNode(1)
n8 = new TreeNode(6)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6 
n3.left = n7
n4.left = n8
low = 6
high = 10
console.log(rangeSumBST(root, low, high))
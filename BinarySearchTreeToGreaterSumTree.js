// Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
// As a reminder, a binary search tree is a tree that satisfies these constraints:
//  The left subtree of a node contains only nodes with keys less than the node's key.
//  The right subtree of a node contains only nodes with keys greater than the node's key.
//  Both the left and right subtrees must also be binary search trees.


// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
  }
 
function bstToGst(root) {
    function helper(curNode, parentValue){
        if (curNode.right){
            curNode.val += helper(curNode.right, parentValue)
        }else{
            curNode.val += parentValue
        }

        if (curNode.left){
            return helper(curNode.left, curNode.val)
        }

        return curNode.val
    }

    if (root){
        helper(root, 0)
    }
    return root
};

// Test cases
root = new TreeNode(4)
n1 = new TreeNode(1)
n2 = new TreeNode(6)
n3 = new TreeNode(0)
n4 = new TreeNode(2)
n5 = new TreeNode(5)
n6 = new TreeNode(7)
n7 = new TreeNode(3)
n8 = new TreeNode(8)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n4.right = n7
n6.right = n8
console.log(bstToGst(root))

root = new TreeNode(0)
n1 = new TreeNode(1)
root.right = n1
console.log(bstToGst(root))
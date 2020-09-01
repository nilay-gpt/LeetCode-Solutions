"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

https://leetcode.com/problems/delete-node-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # when there is no root then return the call, Will help in recursion ahead
        if not root: return
        
        if key > root.val: root.right = self.deleteNode(root.right, key)
        elif key < root.val: root.left = self.deleteNode(root.left, key)
        
        # this will be the case when root.val == key.
        else:
            if not root.left: return root.right
            
            else:
                # find the max value in sub tree. That will be last value in the right side.
                temp = root.left
                while temp.right:
                    temp = temp.right
                
                # replace the current value with value of max of right side.
                root.val = temp.val
                # delete the node once the temp is replaced
                root.left = self.deleteNode(root.left, temp.val)
        
        return root
    
        

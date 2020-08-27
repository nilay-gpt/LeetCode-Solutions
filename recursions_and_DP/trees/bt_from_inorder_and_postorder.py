"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            
            # here is the key, we should do the right insertions first.
            root.right = self.buildTree(inorder[idx+1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root

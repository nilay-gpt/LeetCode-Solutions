"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        if not root: return []
        
        def dfs(node):
            output.append(node.val)
            
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        
        dfs(root)
        return output
        

"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        output = []
        
        def dfs(node):
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            output.append(node.val)

        dfs(root)
        return output

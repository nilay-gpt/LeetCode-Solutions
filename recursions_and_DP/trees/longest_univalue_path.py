"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2
https://leetcode.com/problems/longest-univalue-path/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        
        def dfs(node):
            if not root: return 0
            if node.left: left_path = dfs(node.left)
            if node.right: right_path = dfs(node.right)
            left_check = right_check = 0
            if node.left and node.val == node.left.val:
                left_check = left_path + 1

            if node.right and node.val == node.right.val:
                right_check = right_path + 1
                
            self.output = max(self.output, left_check + right_check)
            return max(left_check, right_check)
            
        dfs(root)
        return self.output

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

https://leetcode.com/problems/binary-tree-maximum-path-sum/
ref link: https://www.youtube.com/watch?v=mOdetMWwtoI
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -float(inf)
        if not root: return -2147483648
        
        def dfs_path_sum(node):
            if not node: return 0
            left = max(0, dfs_path_sum(node.left))
            right = max(0, dfs_path_sum(node.right))
            self.max_sum = max(self.max_sum, left+right+node.val)
            return max(left, right) + node.val
        
        dfs_path_sum(root)
        return self.max_sum
        
        
        

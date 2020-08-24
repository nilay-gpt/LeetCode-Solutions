"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    is_bal = True
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        
        def dfs(node):
            if not node: return 0
            l_dep = dfs(node.left)
            r_dep = dfs(node.right)
            
            if abs(l_dep - r_dep) >=2:
                self.is_bal = False
            
            return max(l_dep, r_dep) + 1
            
        dfs(root)
        return self.is_bal
        

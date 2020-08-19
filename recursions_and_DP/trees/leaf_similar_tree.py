"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

https://leetcode.com/problems/leaf-similar-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.find_leaf(root1) == self.find_leaf(root2)
        
    def find_leaf(self, root):
        if not root: return []
        if not root.left and not root.right: return [root.val]
        return self.find_leaf(root.left) + self.find_leaf(root.right)
    
    
        return self.findleaf(root1) == self.findleaf(root2)
        

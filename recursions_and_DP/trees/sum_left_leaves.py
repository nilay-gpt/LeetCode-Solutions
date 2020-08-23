"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

https://leetcode.com/problems/sum-of-left-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        # summ = 0
        
#         #bfs approch:
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             if node.left and not (node.left.left or node.left.right):
#                     summ += node.left.val
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
                
#         return summ
        
        #dfs approch:
        def dfs(node):
            if not node: return 0
            summ = 0
            if node.left and not (node.left.left or node.left.right):
                summ += node.left.val
            summ += dfs(node.left)
            summ += dfs(node.right)
            return summ
        return dfs(root) 
        

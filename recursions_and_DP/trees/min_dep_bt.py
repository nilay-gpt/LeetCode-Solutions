"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
#         # dfs approch
#         if not root.left or not root.right:
#             return self.minDepth(root.left) + self.minDepth(root.right) + 1
            
#         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        # # BFS approch(early exit.) 
        queue, level = deque([(root, 1)]), 0
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right: return level
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))

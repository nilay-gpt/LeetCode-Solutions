"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursive way
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    
        # bfs way:
#         queue = deque([root])
        
#         while queue:
#             node = queue.popleft()
#             if node:
#                 node.left, node.right = node.right, node.left
#                 queue.append(node.left)
#                 queue.append(node.right)
                
        return root
            

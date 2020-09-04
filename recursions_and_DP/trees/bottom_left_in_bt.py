"""

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

https://leetcode.com/problems/find-bottom-left-tree-value/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # bfs approch
        queue = deque([root])
        self.ans = 0
        while queue:
            node = queue.popleft()
            self.ans = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return self.ans
        
        # DFS approch
#         self.ans = 0
#         self.depth = -1
        
#         def dfs(node, level):
#             if not node: return
#             if level > self.depth:
#                 self.depth = level
#                 self.ans = node.val
                
#             if node.left: dfs(node.left, level+1)
#             if node.right: dfs(node.right, level+1)
        
#         dfs(root, 0)
#         return self.ans
        
        

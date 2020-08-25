"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
   
https://leetcode.com/problems/symmetric-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
    
        def dfs(left, right):
            if left is None and right is None: return True
            if left is None or right is None: return False
            if left.val == right.val:
                out_pair = dfs(left.left, right.right)
                in_pair = dfs(left.right, right.left)
                return out_pair and in_pair
                
            else: return False
        return dfs(root.left, root.right)
    
    # BFS and level order traversal
#         queue = deque([root])
#         while queue:
#             level_list = []
#             for _ in range(0, len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                     level_list.append(node.left.val)
#                 else: level_list.append(None)
#                 if node.right:
#                     queue.append(node.right)
#                     level_list.append(node.right.val)
#                 else: level_list.append(None)
                    
#             if level_list and not(level_list == level_list[::-1]): return False
#         return True

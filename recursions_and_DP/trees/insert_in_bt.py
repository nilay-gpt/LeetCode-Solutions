"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5

https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # recursion method
        if not root: return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
    
        # iterative method
#         if not root: return  TreeNode(val)
#         queue = deque([root])
        
#         while queue:
#             node = queue.popleft()
#             if node.val > val:
#                 if node.left:
#                     queue.append(node.left)
#                 else:
#                     node.left =  TreeNode(val)
#                     break
#             if  node.val < val:
#                 if node.right:
#                     queue.append(node.right)
#                 else:
#                     node.right =  TreeNode(val)
#                     break
#         return root
        
        
  

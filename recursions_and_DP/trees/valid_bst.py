"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        queue = deque([(root, float(-inf), float(inf))])
        
        while queue:
            node, left, right = queue.popleft()
            
            if node.val >= right or node.val <= left:
                return False
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))
                
        return True
        

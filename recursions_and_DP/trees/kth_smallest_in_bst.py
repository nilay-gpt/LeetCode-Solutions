"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        # inorder traverse of bst, returns sorted list.
        def inorder(node):
            if not node: return []
            
            left_val = inorder(node.left)
            root_val = [node.val]
            right_val = inorder(node.right)
            
            return left_val + root_val + right_val
        
        return inorder(root)[k-1]
                

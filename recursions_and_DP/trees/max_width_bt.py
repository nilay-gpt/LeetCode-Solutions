"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

https://leetcode.com/problems/maximum-width-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        queue, width = deque([[root, 1]]), 1

        while queue:
            width = max(width, queue[-1][1] - queue[0][1]+1)
            next_level = []
            
            for node, idx in queue:
                if node.left: next_level.append([node.left, 2*idx])
                if node.right: next_level.append([node.right, 2*idx+1])
                
            queue = next_level
        return width

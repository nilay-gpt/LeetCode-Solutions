"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.


Input: [1,1,1,1,1,null,1]
Output: true

https://leetcode.com/problems/univalued-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: return False
        
        flag = True
        queue = deque([root])
        
        while queue and flag:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    if node.val != node.left.val: flag = False
                    queue.append(node.left)
                    
                if node.right:
                    if node.val != node.right.val: flag = False
                    queue.append(node.right)
                
        return flag

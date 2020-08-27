"""
Given a binary tree, return the sum of values of its deepest leaves.
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

https://leetcode.com/problems/deepest-leaves-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    output = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque([root])
        
        while queue:
            level_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:

                    queue.append(node.right)

        return level_sum

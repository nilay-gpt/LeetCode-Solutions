"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque([root])
        result = deque()
        if not root: return result
        
        while queue:
            current_node, next_level = deque(), deque()
            for node in queue:
                current_node.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
                    
            result.append(sum(current_node)/len(current_node))
            queue = next_level
        return result

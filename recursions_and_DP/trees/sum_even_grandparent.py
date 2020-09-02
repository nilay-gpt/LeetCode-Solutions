"""
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        if not root: return total
        queue = deque([root])
        
        while queue:
            is_even = False
            node = queue.popleft()
            if node.val % 2==0:is_even = True
            
            if node.left:
                queue.append(node.left)
                if is_even:
                    if node.left.left:
                        total += node.left.left.val
                    if node.left.right:
                        total += node.left.right.val
                        
            if node.right:
                queue.append(node.right)
                if is_even:
                    if node.right.left:
                        total += node.right.left.val
                    if node.right.right:
                        total += node.right.right.val
        return total
                        

"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 0
        
        if not root: return count
        
        for child in root.children:
            count = max(count, self.maxDepth(child))
            
        return count + 1

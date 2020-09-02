"""

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = deque()
        if not root: return output
        queue = deque([root])
        
        while queue:
            node = queue.pop()
            output.appendleft(node.val)
            for i in node.children:
                queue.append(i)

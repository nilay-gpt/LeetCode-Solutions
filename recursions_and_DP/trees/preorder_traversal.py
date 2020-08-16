"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

https://leetcode.com/problems/n-ary-tree-preorder-traversal/
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
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root

        queue = deque([root])
        output = []
        
        while queue:
            node = queue.pop()
            output.append(node.val)
            queue.extend(reversed(node.children))
            
        return output


"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

https://leetcode.com/problems/same-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if not (p or q): return True
        # if not (p and q): return False
        # queue = deque([(p, q)])
        # while queue:
        #     n = len(queue)
        #     for _ in range(n):
        #         ln, rn = queue.popleft()
        #         if not ln.val == rn.val:
        #             return False
        #         if ln 
        
        # BFS approch
        if not (p or q): return True
        if not (p and q): return False
        return self.return_node_list(p) == self.return_node_list(q)
        
        
    def return_node_list(self, root):
        output = []
        queue = deque([root])

        while queue:
            for _ in range(0, len(queue)):
                node = queue.popleft()
                output.append(node.val)

                if node.left:
                    queue.append(node.left)
                    output.append(node.left.val)
                else: output.append(None)
                if node.right:
                    queue.append(node.right)
                    output.append(node.right.val)
                else: output.append(None)
                
        return output

        

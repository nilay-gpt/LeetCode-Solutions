"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

https://leetcode.com/problems/cousins-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # bfs approch
        
        queue = deque([root])
        match = set([x,y])
        
        while queue:
            l = len(queue)
            is_x_exists = is_y_exists = False
            for _ in range(l):
                node = queue.popleft()
                if node.val == x: is_x_exists = True
                elif node.val == y: is_y_exists = True
                
                # to check if both x,y dont share the same node
                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == match: return False
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if is_x_exists and is_y_exists: return True

        return False
    
        
        

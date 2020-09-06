"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs approch
        # doing it via flag it save calculations at line 28
        # self.level = -1
        if not root: return []
        queue, self.output = deque([root]), []
        self.flag = True
        
        while queue:
            # self.level += 1
            self.flag = not(self.flag)
            level_list = []
            for i in range(len(queue)):
                node = queue.popleft()
                level_list.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            # if self.level % 2 != 0: self.output.append(level_list[::-1])
            if self.flag: self.output.append(level_list[::-1])
            else:self.output.append(level_list)

        return self.output
        

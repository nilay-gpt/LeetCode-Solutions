"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        queue = deque([root])
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return level

"""
```
 DFS approch:
 
 def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node.left and not node.right:
                return 1
            right = left = 0
            
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            return max(left, right)+1            
    
        return dfs(root)
```


By BFS:
```class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        queue = deque([root])
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return level
```
"""

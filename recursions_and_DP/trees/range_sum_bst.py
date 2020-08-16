"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

https://leetcode.com/problems/range-sum-of-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        def dfs(node):
            left , right, cv = 0, 0, 0
            
            if node.val > L:
                left = dfs(node.left) if node.left else 0
                
            if node.val < R:
                right = dfs(node.right) if node.right else 0
                

            cv = node.val if L <= node.val <= R else 0
            return left + right + cv
                
        return dfs(root)

"""
If a normal tree

```
if not root:
            return 0
            
        queue = deque([root])
        counter = 0
        while queue:
            node = queue.popleft()
            if L <= node.val <= R:
                counter += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return counter
```
"""


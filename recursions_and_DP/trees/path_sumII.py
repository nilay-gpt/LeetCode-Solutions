"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

https://leetcode.com/problems/path-sum-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
        output = []
        if not root: return output
        
        def dfs(root, summ, ll, output):
            if not (root.left or root.right) and summ==root.val:
                ll.append(root.val)
                output.append(ll)

            if root.left: dfs(root.left, summ-root.val, ll+[root.val], output)
            
            if root.right: dfs(root.right, summ-root.val, ll+[root.val], output)
            
        dfs(root, summ, [], output)
        return output

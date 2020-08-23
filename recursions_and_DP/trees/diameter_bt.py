"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # return the depth of the tree

        self.depth = 0
        
        def dfs(node):
            if not node: return 0
            
            left, right = dfs(node.left), dfs(node.right)
            self.depth = max(self.depth, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.depth
            

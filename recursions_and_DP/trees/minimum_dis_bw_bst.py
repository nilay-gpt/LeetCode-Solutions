"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2

https://leetcode.com/problems/minimum-distance-between-bst-nodes/
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    minimum = float('inf')
    def minDiffInBST(self, root):
        stack = []
        
        def dfs(node):
            for val in stack:
                self.minimum = min(self.minimum, abs(val - node.val))
            stack.append(node.val)
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.minimum
    
    

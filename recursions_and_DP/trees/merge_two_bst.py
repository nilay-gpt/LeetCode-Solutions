"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not(root1 or root2): return []
        
        output = []
        # doing inorder traverse, Inorder gives the sorted from on tree
        def dfs(node):
            if node.left:
                dfs(node.left)
            output.append(node.val)
            if node.right:
                dfs(node.right)
            return output
        if root1: dfs(root1)
        if root2: dfs(root2)
        
        return sorted(output)
        

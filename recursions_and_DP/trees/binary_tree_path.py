"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

https://leetcode.com/problems/binary-tree-paths/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        output = []
        if not root: return output
        
        # dfs approch
        def dfs(node, string):
            if not (node.left or node.right):
                output.append(string + str(node.val))
            if node.left:
                dfs(node.left, string+str(node.val) + "->")
            if node.right:
                dfs(node.right, string+str(node.val) + "->")
        
        dfs(root, "")
        return output

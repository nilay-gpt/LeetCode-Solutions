"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].
Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]

https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.flipped = set()
        self.i = 0
        
        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped.add(-1)
                    return
                self.i += 1

                if node.left and node.left.val != voyage[self.i]:
                    self.flipped.add(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        
        if self.flipped and -1 in self.flipped:
            return [-1]
        return self.flipped

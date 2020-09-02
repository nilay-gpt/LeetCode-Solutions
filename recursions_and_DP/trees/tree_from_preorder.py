"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

Example 1:

Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # make a pair where we will store depth-level with the value
        
        pair = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)][::-1]
        
        def make_tree(level):
            if not pair or level != pair[-1][0]: return None
            
            root = TreeNode(pair.pop()[1])
            root.left = make_tree(level+1)
            root.right = make_tree(level+1)
            return root
            
        return make_tree(0)

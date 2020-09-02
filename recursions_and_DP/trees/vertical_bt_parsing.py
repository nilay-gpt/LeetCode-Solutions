"""
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        output = []
        if not root: return output
        # to make a vertical level wise dict
        # we keep track of level in dict because to show in order of asscending.
        order_dict = {}
        def dfs(node, level, col):
            if not node: return 
            if col not in order_dict:
                order_dict[col] = [[node.val, level]]
            else:
                order_dict[col].append([node.val, level])
            if node.left:
                dfs(node.left, level+1, col-1)
            if node.right:
                dfs(node.right, level+1, col+1)
        dfs(root, 0, 0)
        
        for value in sorted(order_dict.keys()):
            level_list = []
            col = sorted(order_dict[value], key = lambda x: (x[1], x[0]))
            for i in col:
                level_list.append(i[0])
            output.append(level_list)
            
        
        return output

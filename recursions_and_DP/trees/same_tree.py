# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # early return approach approch
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return p is q
        
        # BFS approch, mentain output for both the tree and compare the output
#         if not (p or q): return True
#         if not (p and q): return False
#         return self.return_node_list(p) == self.return_node_list(q)
        
        
#     def return_node_list(self, root):
#         output = []
#         queue = deque([root])

#         while queue:
#             for _ in range(0, len(queue)):
#                 node = queue.popleft()
#                 output.append(node.val)

#                 if node.left:
#                     queue.append(node.left)
#                     output.append(node.left.val)
#                 else: output.append(None)
#                 if node.right:
#                     queue.append(node.right)
#                     output.append(node.right.val)
#                 else: output.append(None)
                
#         return output

        

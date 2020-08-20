"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return 
        queue = deque([root])
        output = []
        
        while queue:
            level_list = []
            for _ in range(0, len(queue)):
                node = queue.popleft()
                if not output: output.append([node.val])
                if node.left:
                    queue.append(node.left)
                    level_list.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_list.append(node.right.val)
                    
            if level_list: output.append(level_list)

        return output[::-1]

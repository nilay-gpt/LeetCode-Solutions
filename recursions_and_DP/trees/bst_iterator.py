"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

https://leetcode.com/problems/binary-search-tree-iterator/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        # if not root: return []
        self.asscen_list = self.make_iter_list(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.asscen_list.pop(0)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not(self.asscen_list == [])
    
    def make_iter_list(self, root):
        output = []
        if not root: return []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            output.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return sorted(output)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



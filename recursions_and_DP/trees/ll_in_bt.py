"""
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:

Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

https://leetcode.com/problems/linked-list-in-binary-tree/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head: return True
        if not root: return False
        
        #flatern the LL to one list
        def flat_ll(head):
            str_ll = ""
            current = head
            while current:
                str_ll += str(current.val) + ','
                current = current.next
            return str_ll
        str_ll = flat_ll(head)
        
        #see if flat ll is present in the tree by dfs
        def dfs(node, path_string):
            if not node: return str_ll in path_string
            
            path_string += str(node.val) + ","
            return dfs(node.left, path_string) or dfs(node.right, path_string)
            
        return dfs(root, '')

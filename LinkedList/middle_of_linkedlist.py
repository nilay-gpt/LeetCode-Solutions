"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 
https://leetcode.com/problems/middle-of-the-linked-list/
"""

import json


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#helper methods

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    # lines = readlines()
    while True:
        try:
            # line = lines.next()
            head = stringToListNode("[1,2,3,4,5,6]")

            ret = Solution().middleNode(head)
            print ret.val

            out = listNodeToString(ret)
            break
        except StopIteration:
            break

if __name__ == '__main__':
    main()

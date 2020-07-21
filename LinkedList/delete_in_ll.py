"""
delete the given node from the linkedlist.
ll = [4,5,1,9], node = 5

https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

import json


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


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

def stringToInt(input):
    return int(input)

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
            node = stringToListNode("[4,5,1,9]")
            # line = lines.next()
            n = stringToInt("5")
            print "before node", listNodeToString(node)
            ret = Solution().deleteNode(node)
            out = listNodeToString(node)
            print "after node", out
            break
            if ret is not None:
                print "Do not return anything, modify node in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()

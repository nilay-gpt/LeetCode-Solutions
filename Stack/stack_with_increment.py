"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.maxSize = maxSize
        self.current_len = 1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.current_len <= self.maxSize:
            self.stack.append(x)i
            self.current_len += 1
        return None
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            self.current_len -= 1
            return self.stack.pop()
        else: return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        times = 0
        if self.current_len <= k: times = self.current_len - 1
        else: times = k
        for i in range(0, times):
            self.stack[i] = self.stack[i] + val
        return None
        

if __name__ == "__main__":
    obj = CustomStack(3)
    print obj.push(5)
    print obj.push(4)
    print obj.push(3)
    print "popping-->", obj.pop()
    print obj.stack
    print "popping-->", obj.pop()
    print obj.stack
    print obj.push(6)
    print obj.push(7)
    print obj.push(71)
    print obj.push(51)
    print obj.stack
    print "-----"
    print obj.increment(5,100)
    print obj.stack
    print obj.increment(2,100)
    print obj.stack
    # print "popping-->", obj.pop()
    # print "popping-->", obj.pop()
    # print "popping-->", obj.pop()

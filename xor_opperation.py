"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

 

Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
"""


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xor, cal, i, point = 0, 0, 0, start
        while(n > 0):
            cal = point + 2 * i
            xor = xor ^ cal

            start +=1
            n -=1
            i += 1

        return xor


if __name__ =="__main__":
    a = Solution()
    print a.xorOperation(n = 4, start = 3)

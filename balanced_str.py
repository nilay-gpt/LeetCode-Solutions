"""

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        lcount, rcount, count = 0,0,0
        for i in s:
            if i == "R": rcount += 1
            else: lcount += 1
            if rcount == lcount: lcount, rcount, count = 0,0, count+1
        return count



if __name__ == "__main__":
    a = Solution()
    print a.balancedStringSplit("RLRRRLLRLL")

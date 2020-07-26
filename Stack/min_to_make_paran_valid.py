"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in range(0, len(S)):
            if S[i] == ")" and stack and stack[-1] == "(": stack.pop()
            else: stack.append(S[i])
        return len(stack)


if __name__ == "__main__":
    a = Solution()
    print a.minAddToMakeValid("))")

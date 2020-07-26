"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

https://leetcode.com/problems/longest-valid-parentheses/
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        valid_count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            elif s[i] == ")" and stack and stack[-1] == "(":
                valid_count +=2
                stack.pop()
        return valid_count
    



if __name__ == "__main__":
    a = Solution()
    print a.longestValidParentheses(")(())((())")

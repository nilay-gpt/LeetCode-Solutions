"""

You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        
        for i in s:
            if i == "(":
                stack.append("")
            elif i == ")":
                local = stack.pop()[::-1]
                stack[-1] += local
            else:
                stack[-1] += i
        
        return stack.pop()
                

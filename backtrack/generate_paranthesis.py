"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

https://leetcode.com/problems/generate-parentheses/
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        https://www.youtube.com/watch?v=sz1qaKt0KGQ&ab_channel=BackToBackSWE
        """
        ans = set()
        
        def backtrack(s, openn, close):
            if len(s) == 2*n:
                ans.add(s)
                return
            if openn < n: backtrack(s+'(', openn+1, close)
            
            if close < openn: backtrack(s+')', openn, close+1)
        
        backtrack("", 0, 0)
        return ans

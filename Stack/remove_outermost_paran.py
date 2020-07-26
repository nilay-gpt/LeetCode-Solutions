"""
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

https://leetcode.com/problems/remove-outermost-parentheses/
"""

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        main_list, valid_paran_list, start_window, output = [], [], 0, ""

        for i in range(len(S)):
            if S[i] == "(": valid_paran_list.append("(")
            elif S[i] == ")" and valid_paran_list and valid_paran_list[-1] == "(": valid_paran_list.pop()

            if not valid_paran_list:
                sub_list = S[start_window:i+1]
                main_list.append(sub_list)
                start_window = i+1
        
        for i in main_list:
            output = output+i[1:-1]

        return output
        


if __name__ == "__main__":
    a = Solution()
    print a.removeOuterParentheses("()")

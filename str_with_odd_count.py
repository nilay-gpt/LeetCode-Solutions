"""

Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

 

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
"""


class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        # if n % 2 == 0:
        #     return "a" + "b" * (n - 1)

        # else:
        #     return "a" * (n)

        return "a" + "b" * (n - 1) if n % 2 == 0 else "a" * (n)
        


if __name__ == "__main__":
    a = Solution()
    print a.generateTheString( n = 5)

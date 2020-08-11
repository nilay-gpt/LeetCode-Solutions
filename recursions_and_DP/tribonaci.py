"""

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

https://leetcode.com/problems/n-th-tribonacci-number/
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        #recursion approach
        # if n == 0: return 0
        # elif n==1 or n==2: return 1

        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        # DP solution

        cache = {0: 0, 1: 1, 2: 1}
        if n <= 2:
            return cache[n]

        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2] + cache[i-3]

        return cache[n]


if __name__ == "__main__":
    a = Solution()
    print a.tribonacci(25)

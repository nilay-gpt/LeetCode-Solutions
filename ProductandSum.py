"""
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
"""


class Solution(object):
    def subtractProductAndSum(self, n):
        mul, add = 1, 0
        for i in str(n):
            i = int(i)
            mul *= i
            add += i
        return mul-add


if __name__ == "__main__":
    a = Solution()
    print a.subtractProductAndSum(234)

"""
"""


class Solution:

    def countLargestGroup(self, n):
        dp = {0:0}
        empty_list = [0] * (6*5)

        for i in range(1, n+1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            empty_list[dp[i] - 1] +=1

        return empty_list.count(max(empty_list))


if __name__ == "__main__":

    a = Solution()
    print a.countLargestGroup(2005)

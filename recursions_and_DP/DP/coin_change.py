"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

https://leetcode.com/problems/coin-change/
"""



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Knapsack problem
        # init one array of amount+1 size bcz starting from 0.
        # keep the 1st element as 0, rest +ve inf
        
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        print(dp)
        
        return dp[-1] if dp[-1] != float('inf') else -1

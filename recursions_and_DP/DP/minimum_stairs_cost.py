"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

https://leetcode.com/problems/min-cost-climbing-stairs/
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        DP: start from 2nd and compare the last two min and add to the current value.
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
                 ^
        [1, 100, 2, 1, 1, 100, 1, 1, 100, 1]
        [1, 100, 2, 3, 1, 100, 1, 1, 100, 1]
        [1, 100, 2, 3, 3, 100, 1, 1, 100, 1]
        [1, 100, 2, 3, 3, 103, 1, 1, 100, 1]
        [1, 100, 2, 3, 3, 103, 4, 1, 100, 1]
        [1, 100, 2, 3, 3, 103, 4, 5, 100, 1]
        [1, 100, 2, 3, 3, 103, 4, 5, 104, 1]
        [1, 100, 2, 3, 3, 103, 4, 5, 104, 6]
        """
        # if not cost: return 0
        for i in range(2, len(cost)): cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])

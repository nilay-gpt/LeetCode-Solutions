"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        output = [[0]*col for _ in range(row)]

        #start is always the same.
        output[0][0] = grid[0][0]
        # fill the first col.
        for i in range(1, col):
            output[0][i] = output[0][i-1] + grid[0][i]

        # fill the first row.
        for i in range(1, row):
            output[i][0] =  output[i-1][0] + grid[i][0]

        # do the DP.
        for i in range(1, row):
            for j in range(1, col):
                # take the min of up and the left and add with the current value
                output[i][j] = min(output[i-1][j], output[i][j-1]) + grid[i][j]

        return output[row-1][col-1]

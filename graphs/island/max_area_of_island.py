"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]

https://leetcode.com/problems/max-area-of-island/
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        total_area = 0
        if not grid: return 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    total_area = max(self.dfs(row, col, grid), total_area)
        return total_area


    def dfs(self, row, col, grid):
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]==0:
            return 0

        grid[row][col] = 0
        right = self.dfs(row+1, col, grid)
        left =self.dfs(row-1, col, grid)
        up =self.dfs(row, col+1, grid)
        down =self.dfs(row, col-1, grid)
        return right + left + up + down + 1

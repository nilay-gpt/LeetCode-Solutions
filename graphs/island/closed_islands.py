"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.
Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

https://leetcode.com/problems/number-of-closed-islands/
"""


class Solution:
    def closedIsland(self, grid):
        """
        approch: DFS
        First visted all the corner rows and cols and mark all the 0 as 1 by DFS.
        After this vist the pending of the graph and do the same DFS again.
        """
        total = 0
        row_len = len(grid)
        col_len = len(grid[0])

        for row in range(row_len):
            self.dfs(row, 0, grid)
            self.dfs(row, col_len-1, grid)

        for col in range(row_len):
            self.dfs(0, col, grid)
            self.dfs(row_len-1, col, grid)

        # The trick is to leave all the corner and then do the DFS
        for i in range(1, row_len-1):
            for j in range(1, col_len-1):
                if grid[i][j] == 0:
                    self.dfs(i,j, grid)
                    total += 1
        return total


    def dfs(self, row, col, grid):
        if row<0 or col<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 0:
            return

        grid[row][col] = 1
        self.dfs(row+1, col, grid)
        self.dfs(row-1, col, grid)
        self.dfs(row, col+1, grid)
        self.dfs(row, col-1, grid)

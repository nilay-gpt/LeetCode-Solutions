"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

https://leetcode.com/problems/number-of-islands/
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        total = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(row, col, grid)
                    total +=1
        return total
    
    def dfs(self, row, col, grid):
        if row<0 or col<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1":
            return
        grid[row][col] = "0"
        self.dfs(row+1, col, grid)
        self.dfs(row-1, col, grid)
        self.dfs(row, col+1, grid)
        self.dfs(row, col-1, grid)

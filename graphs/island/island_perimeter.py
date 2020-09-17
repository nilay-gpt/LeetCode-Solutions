"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

https://leetcode.com/problems/island-perimeter/
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        row_len = len(grid)
        col_len = len(grid[0])

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    if row == 0 or grid[row-1][col] == 0: total += 1
                    if col == 0 or grid[row][col-1] == 0: total += 1
                    if col == col_len-1 or grid[row][col+1] == 0: total += 1
                    if row == row_len-1 or grid[row+1][col] == 0: total += 1
        return total

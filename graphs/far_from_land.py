"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

https://leetcode.com/problems/as-far-from-land-as-possible/
"""

from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        max_value = -1
        queue = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    queue.append((row, col))
        if len(queue) == len(grid) * len(grid[0]) or len(queue) == 0: return max_value

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for x, y in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==0:
                        queue.append((x, y))
                        grid[x][y] = 1
            max_value += 1
        return max_value

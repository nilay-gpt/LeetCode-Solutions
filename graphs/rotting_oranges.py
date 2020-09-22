"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

https://leetcode.com/problems/rotting-oranges/
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        minutes = -1
        fresh_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        if not (len(grid) * len(grid[0]) or len(queue)) or fresh_count==0: return 0

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for x, y in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                        queue.append((x,y))
                        grid[x][y] =2
                        fresh_count -=1
            minutes +=1

        return minutes if fresh_count == 0 else -1

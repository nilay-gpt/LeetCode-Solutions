"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]

https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""


from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        # to check if at(0,0) or at the end the way is blocked.
        if grid[0][0] or grid[grid_len-1][grid_len-1]: return -1
        
        #start point with distance 1
        stack = deque([(0,0,1)])
        d = -1
        
        while stack:
            for _ in range(len(stack)):
                row, col, dist = stack.popleft()
                #check if reached the end. It should be and not OR
                if row == grid_len-1 and col == len(grid[0])-1: return dist
                
                # check in all 8 directions
                for ro , co in [(row-1, col), (row-1, col-1), (row-1, col+1), (row, col-1),
                               (row, col+1), (row+1, col-1), (row+1, col+1), (row+1, col)]:
                    if 0<=ro<grid_len and 0<=co<len(grid[0]) and grid[ro][co] == 0:
                        stack.append((ro, co, dist+1))
                        grid[ro][co] = 1
        return d
                    
                

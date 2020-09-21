"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
 
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

https://leetcode.com/problems/01-matrix/
"""

from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    self.bfs(row, col, matrix)
        return matrix

    def bfs(self, row, col, matrix):
            queue = deque([(row, col, 0)])
            while queue:
                ro, co, dist = queue.popleft()
                for r, c in (ro+1, co), (ro-1, co), (ro, co+1), (ro, co-1):
                    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                        if matrix[r][c] == 0:
                            matrix[row][col] = dist+1
                            return
                        else:
                            queue.append((r, c, dist+1))

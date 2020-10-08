"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        row_len, col_len = len(matrix), len(matrix[0])
        pacific_list = [[0]*col_len for _ in range(row_len)]
        atlantic_list = [[0]*col_len for _ in range(row_len)]
        response = []
        
        # for top and bottom rows
        for i in range(col_len):
            self.dfs(0, i, matrix, pacific_list, 0)
            self.dfs(row_len-1, i, matrix, atlantic_list, 0)
            
        # for first and last col
        for j in range(row_len):
            self.dfs(j, 0, matrix, pacific_list, 0)
            self.dfs(j, col_len-1, matrix, atlantic_list, 0)

        for row in range(row_len):
            for col in range(col_len):
                if pacific_list[row][col] and atlantic_list[row][col]:
                    response.append([row,col])
    
        return response
    
    
    def dfs(self, row, col, matrix, s_list, prev):
        if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0])\
        or s_list[row][col] == 1 or matrix[row][col]<prev:
            return
        s_list[row][col] = 1
        
        self.dfs(row+1, col, matrix, s_list, matrix[row][col])
        self.dfs(row-1, col, matrix, s_list, matrix[row][col])
        self.dfs(row, col+1, matrix, s_list, matrix[row][col])
        self.dfs(row, col-1, matrix, s_list, matrix[row][col])

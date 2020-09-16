"""
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.

https://leetcode.com/problems/number-of-enclaves/
"""

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        """
        DFS approch. look all the boundary and if found one there then
        do the DFS and replace to 0 if any connected 1 are there.
        run again and count the remaining 1's in the graph. return the count
        """
        total = 0
        if not A: return total
        row_len = len(A)
        col_len = len(A[0])
        
        #iterate the broder rows
        for r in range(row_len):
            self.revert_to_zero(r, 0, A)
            self.revert_to_zero(r, col_len-1, A)
        
        #iterate the broder col
        for c in range(col_len):
            self.revert_to_zero(0, c, A)
            self.revert_to_zero(row_len-1, c, A)
        
        for row in range(row_len):
            for col in range(col_len):
                if A[row][col] == 1: total += 1
        return total
        
        
    def revert_to_zero(self, row, col, A):
        if row<0 or col<0 or row >=len(A) or col >= len(A[0]) or A[row][col] !=1: 
            return
        A[row][col] = 0
        self.revert_to_zero(row-1, col, A)
        self.revert_to_zero(row+1, col, A)
        self.revert_to_zero(row, col-1, A)
        self.revert_to_zero(row, col+1, A) 
        return

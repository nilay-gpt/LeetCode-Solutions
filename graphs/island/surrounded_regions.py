"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

https://leetcode.com/problems/surrounded-regions/
exp: https://www.youtube.com/watch?v=WhJqV5KAGEE&ab_channel=PersistentProgrammer
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Approch: DFS
        > Take all the corners(rows and col) and mark I if any O is there.
          Also, mark I to all the connected O's to that.
        > After the DFS is done mark all the o's to x and I's to O in the board.
        """
        if not board: return board
        row_len = len(board)
        col_len = len(board[0])
        
        for r in range(row_len):
            self.mark_invalid(r, 0, board)
            self.mark_invalid(r, col_len-1, board)
            
        for c in range(col_len):
            self.mark_invalid(0, c, board)
            self.mark_invalid(row_len-1, c, board)
            
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O": board[row][col] = 'X'
                if board[row][col] == "I": board[row][col] = 'O'
        return
        
    def mark_invalid(self, row, col, board):
        #base condition
        if row< 0 or col< 0 or row >= len(board) or col >= len(board[0]) or board[row][col] !='O': 
            return 
        board[row][col] = "I"
        self.mark_invalid(row-1, col, board)
        self.mark_invalid(row+1, col, board)
        self.mark_invalid(row, col-1, board)
        self.mark_invalid(row, col+1, board)
        return





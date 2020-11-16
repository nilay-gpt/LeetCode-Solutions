"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

https://www.youtube.com/watch?v=p4jExm5Zf6Q&ab_channel=babybear4812
https://leetcode.com/problems/candy-crush/
"""


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        1> sliding window of size = 3(given).
        2> Traverse all the row and see if all the (abs) values same in the
            window. If yes then make it negative. then move forward.
        3> Repeat 2 for the columns also.
        4> Gravity: traverse on all the coloumn and move down by shifting all
            all zero to the top
        5> Repeat till True
        """
        
        # base condition
        if not board: return board
        
        stable = True
        window = 2 #(staring from 0)
        
        #Point 2
        for r in range(len(board)):
            for c in range(len(board[0]) - window):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])
                if num1 == num2 and num2==num3 and num1!=0:
                    board[r][c] = -num1
                    board[r][c+1] = -num2
                    board[r][c+2] = -num3
                    stable = False
        #Point 3
        for c in range(len(board[0])):
            for r in range(len(board) - window):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
                if num1 == num2 and num2==num3 and num1!=0:
                    board[r][c] = -num1
                    board[r+1][c] = -num2
                    board[r+2][c] = -num3
                    stable = False
        
        #Point 4
        if not stable:
            for c in range(len(board[0])):
                idx = len(board)-1
                #Start from bottom and end at the top
                for r in range(len(board)-1, -1, -1):
                    if board[r][c]>0:
                        board[idx][c] = board[r][c]
                        idx -= 1
                
                #from the last -1 update everything to 0 till the top
                for r in range(idx, -1, -1):
                    board[r][c] = 0
        
        return board if stable else self.candyCrush(board)

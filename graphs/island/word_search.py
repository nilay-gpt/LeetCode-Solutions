"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

https://leetcode.com/problems/word-search/
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, word, row, col):
                    return True
        return False


    def dfs(self, board, word, row, col):

        if len(word) == 0: return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[0]: return False

        #as the first char is matched so keep it in temp and replace it with "#" to avoind revist
        temp = board[row][col]
        board[row][col] = "#"

        result = self.dfs(board, word[1:], row+1, col) or self.dfs(board, word[1:], row-1, col) \
        or self.dfs(board, word[1:], row, col+1) or self.dfs(board, word[1:], row, col-1)

        board[row][col] = temp

        return result

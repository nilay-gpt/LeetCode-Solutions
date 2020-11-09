"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]

https://leetcode.com/problems/minimum-falling-path-sum/
"""


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        # start from the 2row and check till the end.
        # for 4+min((i-1, j-1), (i-1, j), (i-1, j+1))
        
        if not A: return 0

        for i in range(1, len(A)):
            for j in range(len(A[0])):
                # for the 1st col, when can reach to only two above points 
                if j == 0:
                    A[i][j] = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i-1][j+1]))
                # for the 1st col, when can reach to only two above points 
                elif j == len(A[0])-1:
                    A[i][j] = min((A[i][j] + A[i-1][j]), (A[i][j] + A[i-1][j-1]))
                    
                else:
                    A[i][j] = min((A[i][j] +  A[i-1][j-1]), (A[i][j] + A[i-1][j]), (A[i][j] + A[i-1][j+1]))
                    
        return min(A[-1])
    

"""

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

https://leetcode.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        https://www.youtube.com/watch?v=AuYujVj646Q&ab_channel=TECHDOSE
        3 main things:
        Insert: [i][j-1] #when iserted in the start the ith pointer remains at the same and j decreases by 1(loop working)
        Delete: [i-1][j] # when deleted one in i then ith postions goes back to one position.
        update: [i-1][j-1] # update and both pointers goes back by one position.
        
        When last char is same then:
                [i-1][j-1]
        """
        m, n = len(word1), len(word2)
        # if any array is empty
        if m*n == 0: return m+n
        result = [[0] * (n+1) for i in range(m+1)]
        
        # init the boundaries
        for i in range(m+1): result[i][0] = i
        for j in range(n+1): result[0][j] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    result[i][j] = result[i-1][j-1]
                else:
                    result[i][j] = 1+ min((result[i][j-1]),
                                       (result[i-1][j]),
                                       (result[i-1][j-1]))
                    
        return result[m][n]
                    
                       

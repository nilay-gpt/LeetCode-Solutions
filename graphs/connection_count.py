"""
You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

https://leetcode.com/problems/count-servers-that-communicate/
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)                #from the 1st constraints
        cols = len(grid[0])             #from the 2nd constraints
        
        #if any rows and col is 0 then return 0
        if not (rows and cols): return 0
        
        connected_count = 0             #num of connected computers
        connected_per_row = [0] * rows  #all 0's in start, to keep track
        connected_per_col = [0] * cols  #all 0's in start, to keep track
        points = []                     #points where the connection is available
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:                  #if any cell is 1(connected)
                    connected_per_row[row] += 1     #increase the row count
                    connected_per_col[col] += 1     #increase the col count
                    points.append((row, col))

        #to get the connected count traverse the points list.
        for x, y in points:
            #if there are more than one computer in the row or col, increase.
            if connected_per_row[x]>1 or connected_per_col[y]>1:
                connected_count +=1
        return connected_count

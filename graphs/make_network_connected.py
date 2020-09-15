"""
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1. 


Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0

https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""
class UnionFind(object):
    def __init__(self):
        # Initialise the parent dict as empty
        self.parent = {}
    
    def make_set(self, x):
        self.parent[x] = x
    
    def find(self, x):
        # When the new computer is coming in the network, then it will be its own parent.
        if x not in self.parent:
            self.make_set(x)
            return x

        elif self.parent[x] == x:
            return x

        # iteration to get the parent if above two conditions are not satisfied.
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        """
        if the parent of two are diffent and it is coming from the same list([x,y]).
        this refers that x is connected to the y or x is the parent of y
        """
        if x_set != y_set:
            self.parent[x_set] = y_set
            return True
        return False


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        redundant_connection = 0
        count = n

        uf = UnionFind()
        for x, y in connections:
            # when two computers are connected to the same root or parent then there is a redundant connection.
            if not uf.union(x, y):
                redundant_connection += 1
            else:
                # And when it is not connected to the same network or the parent is different, then reduce the count.
                count -= 1

        if redundant_connection >= count-1:
            return count-1
        return -1
        

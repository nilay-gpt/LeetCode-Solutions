"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
     
https://leetcode.com/problems/redundant-connection-ii/
"""


# similar to problem 684 of finding a cycle in the graph but in this one extra step is to
# find the node with inorder 2 also. need to take care of two cases here.

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        elif self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x,y):
        x_set = self.find(x)
        y_set = self.find(y)

        if x_set != y_set:
            self.parent[x_set] = y_set
            return True
        return False


class Solution:
    def findRedundantDirectedConnection(self, edges):

        cand1, cand2, point_to = None, None, {}
        for node1, node2 in edges:
            if node2 in point_to: 
                cand1, cand2 = point_to[node2], [node1, node2]
                break
            point_to[node2] = [node1, node2]

        uf = UnionFind()
        for node1, node2 in edges:
            if [node1, node2] == cand2: continue
            if not uf.union(node1, node2):
                if cand1:
                    return cand1
                return [node1, node2]
        return cand2

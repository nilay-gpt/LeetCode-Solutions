"""
Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

https://leetcode.com/problems/all-paths-from-source-to-target/
"""

from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # BFS approach
        if not graph: return []
        queue = deque([[0]])
        result = []

        while queue:
            node = queue.popleft()
            if node[-1] == len(graph)-1:
                result.append(node)
            else:
                for i in graph[node[-1]]:
                    queue.append(node + [i])

        return result
